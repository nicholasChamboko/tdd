import pandas as pd
import numpy as np


def clean_dataframe(df):
    """
        Removing duplicate rows, filling null values with 0
        Converting column names to lowercase
    """

    df = df.copy()              # Copy the dataframe
    df = df.drop_duplicates()   # Dropping duplicates
    df = df.fillna(0)  # Filling null values with 0

    # list comprehension that converts columns to lowercase
    df.columns = [col.lower() for col in df.columns]
    return df


def calculate_metrics(df, value_column):
    """
        Calculate metrics based on a numeric column
    """
    return {
        'mean': df[value_column].mean(),  # Mean value calculation
        'median': df[value_column].median(),  # Calculating the median
        'std': df[value_column].std(),  # Calculating data standard deviation
        'min': df[value_column].min(),
        'max': df[value_column].max()
    }
