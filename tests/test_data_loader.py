import pandas as pd
import pytest
from src.utils.data_loader import load_raw_data

def test_load_raw_data_success(tmp_path):
    # Simulate a valid CSV file
    sample_data = """sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,Iris-setosa
6.2,3.4,5.4,2.3,Iris-virginica
"""
    temp_file = tmp_path / "iris_sample.csv"
    temp_file.write_text(sample_data)

    df = load_raw_data(str(temp_file))

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 5)
    assert "species" in df.columns
