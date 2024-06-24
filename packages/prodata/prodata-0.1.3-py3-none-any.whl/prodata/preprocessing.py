import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder



def impute_missing_data(df):
    # Identify missing data in each column and impute based on column type
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]):
            # Check if the column has text-like content (custom condition)
            if df[col].apply(lambda x: isinstance(x, str) and len(x.split()) > 5).any():
                continue  # Skip imputation for columns with text-like content
            
           
        
        elif pd.api.types.is_numeric_dtype(df[col]):
            # Impute missing values in numeric columns
            if df[col].isnull().any():
                if df[col].skew() > 1 or df[col].skew() < -1:
                    # Impute with median if skewness is high
                    median_value = df[col].median()
                    df[col] = df[col].fillna(median_value)
                else:
                    # Impute with mean if skewness is not high
                    mean_value = df[col].mean()
                    df[col] = df[col].fillna(mean_value)

        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            # Skip imputation for datetime columns
            continue

        else:
            # Impute missing values in other columns (e.g., category)
            mode_value = df[col].mode().iloc[0]
            df[col] = df[col].fillna(mode_value)

    return df



def treat_outliers(df):
    # Capping method
    for col in df.select_dtypes(include=['number']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        
        df[col] = df[col].apply(lambda x: lower_bound if x < lower_bound else (upper_bound if x > upper_bound else x))
        # Add other outlier treatment methods as needed
    return df




def encode_categorical_columns(df, method='label'):
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    if method == 'label':
        label_encoder = LabelEncoder()
        for col in categorical_cols:
            df[col + '_encoded'] = label_encoder.fit_transform(df[col].astype(str))
    
    elif method == 'one-hot':
        df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    return df





def draw_boxplots(df):
    # Get numerical columns
    numerical_cols = df.select_dtypes(include=['number']).columns
    
    # Plot boxplots for each numerical column
    for col in numerical_cols:
        plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.show()
