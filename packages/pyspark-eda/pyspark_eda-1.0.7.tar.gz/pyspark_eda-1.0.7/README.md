# pyspark_eda

`pyspark_eda` is a Python library for performing exploratory data analysis (EDA) using PySpark. It offers functionalities for both univariate and bivariate analysis, handling missing values, outliers, and visualizing data distributions.

## Features

- **Univariate analysis:** Analyze numerical and categorical columns individually.
- **Bivariate analysis:** Includes correlation, Cramer's V, and ANOVA.
- **Automatic handling:** Deals with missing values and outliers seamlessly.
- **Visualization:** Provides graphical representation of data distributions and relationships.

## Installation
You can install `pyspark_eda` via pip:

```bash
pip install pyspark_eda
```

## Example Usage
### Univariate Analysis

```python
from pyspark.sql import SparkSession
from pyspark_eda import get_univariate_analysis

# Initialize Spark session
spark = SparkSession.builder.appName('DataAnalysis').getOrCreate()

# Load your data into a PySpark DataFrame
df = spark.read.csv('your_data.csv', header=True, inferSchema=True)

# Perform univariate analysis
get_univariate_analysis(df, id_list=['id_column'], print_graphs=1)
```

### Bivariate Analysis

```python
from pyspark.sql import SparkSession
from pyspark_eda import get_bivariate_analysis

# Initialize Spark session
spark = SparkSession.builder.appName('DataAnalysis').getOrCreate()

# Load your data into a PySpark DataFrame
df = spark.read.csv('your_data.csv', header=True, inferSchema=True)

# Perform bivariate analysis
get_bivariate_analysis(df,table_name="bivariate_analysis_results", print_graphs=1, id_columns=['id_column'], correlation_analysis=1, cramer_analysis=1, anova_analysis=1)
```

## Functions
## get_univariate_analysis
### Parameters
- **df** (*DataFrame*): The input PySpark DataFrame.
- **id_list** (*list*, optional): List of columns to exclude from analysis.
- **print_graphs** (*int*, optional): Whether to print graphs (1 for yes, 0 for no),default value is 0.

### Description
Performs univariate analysis on the DataFrame and prints summary statistics and visualizations.

## get_bivariate_analysis
### Parameters
- **df** (*DataFrame*): The input PySpark DataFrame.
- **table_name** (*str*): The base table name to save the results
- **print_graphs** (*int, optional*): Whether to print graphs (1 for yes, 0 for no),default value is 0.
- **id_columns** (*list, optional*): List of columns to exclude from analysis.
- **correlation_analysis** (*int, optional*): Whether to perform correlation analysis (1 for yes, 0 for no),default value is 1.
- **cramer_analysis** (*int, optional*): Whether to perform Cramer's V analysis (1 for yes, 0 for no), default value is 1.
- **anova_analysis** (*int, optional*): Whether to perform ANOVA analysis (1 for yes, 0 for no),default value is 1.

### Description
Performs bivariate analysis on the DataFrame, including correlation, Cramer's V, and ANOVA.

## Contact
- **Author:** Tanya Irani
- **Email:** tanyairani22@gmail.com