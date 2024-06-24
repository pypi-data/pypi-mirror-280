dataproc

dataproc is a Python library designed to streamline common data preprocessing tasks, making it easier for data scientists and analysts to prepare their datasets for analysis and modeling. This library provides functions to handle missing data, treat outliers, encode categorical variables, and visualize data distribution using boxplots.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installation
You can install dataproc using pip:
pip install dataproc

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from dataproc.preprocessing import impute_missing_data, treat_outliers, encode_categorical_columns, draw_boxplots

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions:

1. impute_missing_data(df)
Purpose: Imputes missing values in a DataFrame. (Numerical and categorical columns)

Parameters:
df (DataFrame): Input DataFrame with missing values. Any columns that do not wish to be treated, can be left out and then the
dataframe can be put as an input parameter.

Usage: Handles missing data by imputing based on column type (numeric, categorical). Datetime and string/text datatypes are
not treated. If the object/categorical column has more than five words, it will be treated as a text/string column and missing values will not be imputed. Numeric datatype - if column has outliers, median is used to impute missing data, if not, mean is used. 
For categorical columns, mode of the column is used to impute missing data within that particular column.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2. treat_outliers(df)
Purpose: Treats outliers in numerical columns using the capping method.

Parameters:
df (DataFrame): Input DataFrame with numerical columns. Any columns which are not to be treated should be dropped first.

Usage: Adjusts extreme values in numerical data to improve robustness in statistical analysis and modeling. Interquartile methos is used, where values lower than lower limit are capped to lower limit and values greater than upper limit are capped to upper limit.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3. encode_categorical_columns(df, method='label')
Purpose: Encodes categorical variables in a DataFrame.

Parameters:
df (DataFrame): Input DataFrame with categorical columns. Make sure to not input any column having text or string, this is only used for categories and not for long text, etc.

method (str, optional): Method of encoding ('label' for Label Encoding, 'one-hot' for One-Hot Encoding). Default is 'label'.

Usage: Converts categorical variables into numerical representations for machine learning algorithms. Supports both Label Encoding and One-Hot Encoding.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4. draw_boxplots(df)
Purpose: Visualizes the distribution of numerical data using boxplots. Also for the visusalization of outliers.

Parameters:
df (DataFrame): Input DataFrame with numerical columns.

Usage: Generates boxplots for each numerical column in the DataFrame, aiding in understanding data distribution and identifying outliers.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example:
# Example usage of dataproc functions
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [10, 20, None, 40, 50],
    'D': ['A', 'B', 'A', 'C', 'B']
})

# Impute missing data
df_cleaned = impute_missing_data(df)

# Treat outliers
df_cleaned = treat_outliers(df)

# Encode categorical columns using Label Encoding
df_encoded = encode_categorical_columns(df, method='label')

# Draw boxplots
draw_boxplots(df)

plt.show()  # Display the plots

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

License:
This project is licensed under the MIT License - see the LICENSE file for details.


Contributing:
Contributions are welcome! Please feel free to submit issues and pull requests.