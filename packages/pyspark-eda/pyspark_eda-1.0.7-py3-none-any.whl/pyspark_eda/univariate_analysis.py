from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
import matplotlib.pyplot as plt
from .utils import round_off

def get_univariate_analysis(df, print_graphs=0, id_list=None):
    spark = SparkSession.builder.getOrCreate()

    # Drop the ID column if provided
    if id_list:
        df = df.drop(*id_list)

    # Define schema for the final summary DataFrames
    numerical_summary_schema = StructType([
        StructField('column', StringType(), nullable=False),
        StructField('total_count', IntegerType(), nullable=False),
        StructField('min', DoubleType(), nullable=True),
        StructField('max', DoubleType(), nullable=True),
        StructField('mean', DoubleType(), nullable=True),
        StructField('mode', DoubleType(), nullable=True),
        StructField('null_percentage', StringType(), nullable=True),
        StructField('skewness', DoubleType(), nullable=True),
        StructField('kurtosis', DoubleType(), nullable=True),
        StructField('stddev', DoubleType(), nullable=True),
        StructField('q1', DoubleType(), nullable=True),
        StructField('q2', DoubleType(), nullable=True),
        StructField('q3', DoubleType(), nullable=True),
        StructField('mean_plus_3std', DoubleType(), nullable=True),
        StructField('mean_minus_3std', DoubleType(), nullable=True),
        StructField('outlier_percentage', StringType(), nullable=True)
    ])

    categorical_summary_schema = StructType([
        StructField('column', StringType(), nullable=False),
        StructField('total_count', IntegerType(), nullable=False),
        StructField('null_percentage', StringType(), nullable=True),
        StructField('frequency_distribution', StringType(), nullable=True)
    ])

    # Initialize empty DataFrames with the defined schema
    numerical_summary_df = spark.createDataFrame(spark.sparkContext.emptyRDD(), schema=numerical_summary_schema)
    categorical_summary_df = spark.createDataFrame(spark.sparkContext.emptyRDD(), schema=categorical_summary_schema)

    # Mapper function for numerical columns
    def map_numerical(column):
        total_count = df.count()
        min_value = float(df.select(F.min(column)).first()[0])
        max_value = float(df.select(F.max(column)).first()[0])
        mean_value = float(df.filter(~df[column].isNull()).select(F.round(F.mean(column), 3)).first()[0])
        mode_value = float(df.filter(~df[column].isNull()).groupBy(column).count().orderBy(F.desc('count')).select(column).first()[0])
        null_count = df.filter(df[column].isNull()).count()
        null_percentage = round_off((null_count / total_count) * 100)
        skewness_value = float(df.filter(~df[column].isNull()).select(F.round(F.skewness(column), 3)).first()[0])
        kurtosis_value = float(df.filter(~df[column].isNull()).select(F.round(F.kurtosis(column), 3)).first()[0])
        stddev_value = float(df.filter(~df[column].isNull()).select(F.round(F.stddev(column), 3)).first()[0])
        q1, q2, q3 = df.filter(~df[column].isNull()).approxQuantile(column, [0.25, 0.5, 0.75], 0.001)
        q1, q2, q3 = float(round_off(q1)), float(round_off(q2)), float(round_off(q3))
        mean_plus_3std = float(round_off(mean_value + 3 * stddev_value))
        mean_minus_3std = float(round_off(mean_value - 3 * stddev_value))
        outlier_count = df.filter((F.col(column) > mean_plus_3std) | (F.col(column) < mean_minus_3std)).count()
        outlier_percentage = round_off((outlier_count / total_count) * 100)

        return (column, total_count, min_value, max_value, mean_value, mode_value, f"{null_percentage}%", skewness_value, kurtosis_value, stddev_value, q1, q2, q3, mean_plus_3std, mean_minus_3std, f"{outlier_percentage}%")

    # Mapper function for categorical columns
    def map_categorical(column):
        total_count = df.count()
        null_count = df.filter(df[column].isNull()).count()
        null_percentage = round_off((null_count / total_count) * 100, 3)
        frequencies = df.groupBy(column).count().orderBy(F.desc('count')).select(column, F.col('count').alias('frequency')).collect()
        frequencies_dict = {row[column]: row['frequency'] for row in frequencies}

        return (column, total_count, f"{null_percentage}%", str(frequencies_dict))

    # Apply mappers
    numerical_columns = [col for col, dtype in df.dtypes if dtype in ['int', 'double']]
    categorical_columns = [col for col, dtype in df.dtypes if dtype == 'string']

    numerical_mapped = [map_numerical(col) for col in numerical_columns]
    categorical_mapped = [map_categorical(col) for col in categorical_columns]

    # Reducer for numerical columns (identity function since we already have the final results in the mapper)
    def reduce_numerical(mapped_values):
        return spark.createDataFrame(mapped_values, schema=numerical_summary_schema)

    # Reducer for categorical columns (identity function since we already have the final results in the mapper)
    def reduce_categorical(mapped_values):
        return spark.createDataFrame(mapped_values, schema=categorical_summary_schema)

    # Apply reducers
    numerical_summary_df = reduce_numerical(numerical_mapped)
    categorical_summary_df = reduce_categorical(categorical_mapped)

    print("Numerical Columns Summary:")
    numerical_summary_df.show(truncate=False)

    print("Categorical Columns Summary:")
    categorical_summary_df.show(truncate=False)

    if print_graphs:
        # Show histograms for numerical columns
        for column in numerical_columns:
            plt.figure(figsize=(6, 4))
            data = df.select(column).rdd.flatMap(lambda x: x).collect()
            _, bins, _ = plt.hist(data, bins='auto', edgecolor='black')  # 'auto' will use the Freedman-Diaconis rule
            plt.title(f'{column} Histogram')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.tight_layout()
            plt.show()

        # Plot frequency distribution for categorical data
        for column in categorical_columns:
            frequencies_dict = eval(categorical_summary_df.filter(F.col("column") == column).select("frequency_distribution").first()[0])
            plt.bar(frequencies_dict.keys(), frequencies_dict.values())
            plt.title(f"Frequency Distribution of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
            plt.tight_layout()
            plt.show()