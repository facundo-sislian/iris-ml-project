import pandas as pd

EXPECTED_COLUMNS = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

def load_raw_data(filepath: str) -> pd.DataFrame:
    """
    Load the Iris dataset from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded dataset.

    Raises:
        ValueError: If required columns are missing.
    """
    df = pd.read_csv(filepath)

    if not all(col in df.columns for col in EXPECTED_COLUMNS):
        raise ValueError(f"CSV is missing required columns. Found: {df.columns.tolist()}")

    return df
