from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql.functions import col
from scipy.stats import chi2_contingency, f_oneway
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .utils import round_off

def get_bivariate_analysis(df, print_graphs=False, id_columns=None, correlation_analysis=True, cramer_analysis=True, anova_analysis=True):
    spark = SparkSession.builder.getOrCreate()

    # Drop the ID column if provided
    if id_columns:
        df = df.drop(*id_columns)

    # Drop columns with all null values
    not_null_columns = [col for col in df.columns if df.filter(df[col].isNotNull()).count() == 0]
    df = df.drop(*not_null_columns)

    # Get numerical columns and categorical columns
    numerical_columns = [col for col, dtype in df.dtypes if dtype in ['int', 'double']]
    categorical_columns = [col for col, dtype in df.dtypes if dtype == 'string']

    # Schema definitions for result DataFrames
    correlation_schema = StructType([
        StructField('Column_1', StringType(), nullable=False),
        StructField('Column_2', StringType(), nullable=False),
        StructField('CorrelationCoefficient', DoubleType(), nullable=True)
    ])

    cramer_schema = StructType([
        StructField('Column_1', StringType(), nullable=False),
        StructField('Column_2', StringType(), nullable=False),
        StructField("Cramer's V", DoubleType(), nullable=True)
    ])

    anova_schema = StructType([
        StructField('Numerical_Column', StringType(), nullable=False),
        StructField('Categorical_Column', StringType(), nullable=False),
        StructField('F_Value', DoubleType(), nullable=True),
        StructField('P_Value', DoubleType(), nullable=True)
    ])

    # Initialize empty DataFrames with the defined schema
    correlation_df = spark.createDataFrame(spark.sparkContext.emptyRDD(), schema=correlation_schema)
    cramer_df = spark.createDataFrame(spark.sparkContext.emptyRDD(), schema=cramer_schema)
    anova_df = spark.createDataFrame(spark.sparkContext.emptyRDD(), schema=anova_schema)

    # Numerical vs numerical analysis - correlation coefficient
    '''The correlation coefficient is a statistical measure of the strength of a linear relationship between two variables.
    Its values can range from -1 to 1.
    A correlation coefficient of -1 describes a perfect negative, or inverse, correlation.
    A coefficient of 1 shows a perfect positive correlation, or a direct relationship.
    A correlation coefficient of 0 means there is no linear relationship.'''
    if correlation_analysis and numerical_columns:
        correlations = []
        for i in range(len(numerical_columns)):
            for j in range(i + 1, len(numerical_columns)):
                col1 = numerical_columns[i]
                col2 = numerical_columns[j]
                corr = df.stat.corr(col1, col2)
                correlations.append((col1, col2, corr))
        correlation_df = spark.createDataFrame(correlations, schema=correlation_schema)
    
    print("Numerical Features Correlation Coefficients:")
    correlation_df.show(truncate=False)
    
    # Categorical vs categorical analysis - Cramer's V
    '''Cramer’s V is a measure of the strength of association between two nominal variables. It ranges from 0 to 1 where:
    0 indicates no association between the two variables. 1 indicates a perfect association between the two variables.'''
    if cramer_analysis and categorical_columns and len(categorical_columns) >= 2:
        def cramers_v(contingency_table):
            chi2 = chi2_contingency(contingency_table)[0]
            n = contingency_table.sum()
            return np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))

        cramer_results = []
        for i in range(len(categorical_columns)):
            for j in range(i + 1, len(categorical_columns)):
                col1 = categorical_columns[i]
                col2 = categorical_columns[j]

                # Filter out rows with null values in either column
                filtered_df = df.filter(col(col1).isNotNull() & col(col2).isNotNull())

                # Calculate the contingency table
                contingency_table = filtered_df.groupBy(col1, col2).count().groupBy(col1).pivot(col2).sum("count").fillna(0)

                # Get the collected data and column names
                data = contingency_table.collect()
                column_names = contingency_table.columns[1:]

                # Construct the numpy array
                counts = np.array([row[1:] for row in data], dtype=int)

                # Filter out rows and columns with all zeros
                counts = counts[~(counts == 0).all(1)]
                counts = counts[:, ~(counts == 0).all(0)]

                if counts.size > 0:  # Check if the matrix is non-empty
                    v = cramers_v(counts)
                    cramer_results.append((col1, col2, round_off(float(v))))

        cramer_df = spark.createDataFrame(cramer_results, schema=cramer_schema)
        cramer_df = cramer_df.sort(col("Cramer's V").desc())

        print("\nCategorical Features Cramer's V:")
        cramer_df.show(truncate=False)

    # Numerical vs categorical analysis - ANOVA
    '''ANOVA (Analysis of Variance) tests whether there are significant differences between the means of different groups.
    F-Value: A higher F-value indicates greater variance between groups compared to within groups.
    P-Value: A P-value < 0.05 typically indicates significant differences between group means,
    suggesting the categorical variable impacts the numerical variable.'''
    if anova_analysis and numerical_columns and categorical_columns:
        anova_results = []
        for num_col in numerical_columns:
            for cat_col in categorical_columns:
                # Ensure numerical column is cast to DoubleType
                df = df.withColumn(num_col, col(num_col).cast('double'))

                # Group by categorical column and compute summary statistics
                summary_stats = df.groupBy(cat_col).agg(
                    F.mean(num_col).alias('mean'),
                    F.count(num_col).alias('count')
                )

                # Collect the summary statistics into a list
                summary_list = summary_stats.collect()

                # Overall mean for the numerical column
                overall_mean = df.select(F.mean(col(num_col)).alias('mean')).collect()[0]['mean']

                # Sum of squares between groups (SSB)
                ssb = sum(row['count'] * (row['mean'] - overall_mean) ** 2 for row in summary_list)

                # Sum of squares within groups (SSW)
                ssw = df.withColumn('squared_diff', (col(num_col) - overall_mean) ** 2).agg(F.sum('squared_diff').alias('ssw')).collect()[0]['ssw']

                # Degrees of freedom
                df_b = len(summary_list) - 1
                df_w = df.count() - len(summary_list)

                # F-value
                f_val = (ssb / df_b) / (ssw / df_w)

                # P-value
                category_groups = [df.filter(col(cat_col) == row[cat_col]).select(num_col).rdd.flatMap(lambda x: x).collect() for row in summary_list]
                p_val = f_oneway(*category_groups)[1]

                # Append ANOVA results
                anova_results.append((num_col, cat_col, round_off(float(f_val),4), round_off(float(p_val),4)))

        anova_df = spark.createDataFrame(anova_results, schema=anova_schema)
        anova_df = anova_df.withColumn('P_Value', col('P_Value'))
        anova_df = anova_df.sort(col('P_Value'))

        print("\nNumerical vs Categorical ANOVA Results:")
        anova_df.show(truncate=False)

    # Shows scatter plot if the user wants
    if print_graphs:
        pandas_df = df.select(numerical_columns).toPandas()
        for i in range(len(numerical_columns)):
            for j in range(i + 1, len(numerical_columns)):
                col1 = numerical_columns[i]
                col2 = numerical_columns[j]
                plt.figure(figsize=(5, 3))
                sns.scatterplot(x=pandas_df[col1], y=pandas_df[col2])
                plt.title(f'Scatter Plot between {col1} and {col2}')
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.show()