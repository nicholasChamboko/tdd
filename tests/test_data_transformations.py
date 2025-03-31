import pytest
import pandas as pd
import numpy as np
from src.data_transformations import clean_dataframe, calculate_metrics


def test_clean_dataframe_removes_duplicates():
    # Arrange
    data = pd.DataFrame({
        'ID': [1, 2, 2, 3],
        'Value': [10, 20, 20, 30]
    })
    # Act
    result = clean_dataframe(data)

    # Assert
    assert len(result) == 3
    assert len(result.column) == ['id', 'value']


def test_clean_dataframe_fills_nulls():
    # Arrange
    data = pd.DataFrame({
        'ID': [1, 2, 3],
        'Value': [10, None, 30]
    })

    # Act
    result = clean_dataframe(data)
    # Assert
    assert result['value'].isna().sum() == 0
    assert result.loc[1, 'value'] == 0


def test_calculate_metrics():
    # Arrange
    data = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'value': [10, 20, 30, 40, 50]
    })


# Act
metrics = calculate_metrics(data, 'value')

# Assert
assert metrics['mean'] == 30
assert metrics['median'] == 30
assert metrics['min'] == 10
assert metrics['max'] == 50
assert metrics['std'] == pytest.approx(15.81, 0.01)
