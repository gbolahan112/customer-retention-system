import pandas as pd

def load_data():
    """
    Load lagos rent dataset
    """
    df = pd.read_csv("data/lagos_rent.csv")
    return df