import pytest
import pandas as pd
import os


@pytest.fixture
def sample_data():
    """fixture provides the sample data input for tests"""
    return pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'value': [10.5, 20.1, None, 15.7, 8.9]
    })


@pytest.fixture
def database_connection():
    """Fixture for database connection testing"""
    import sqlite3
    conn = sqlite3.connect(':memory')
    yield conn
    conn.close()
