import pandas as pd

def load_data():

    df = pd.read_csv("data/churn.csv")

    """
    Load lagos rent dataset
    """
    df = pd.read_csv("data/lagos_rent.csv")

    return df