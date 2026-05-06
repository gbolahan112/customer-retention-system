import pandas as pd

def load_data():
    df = pd.read_csv("data/churn.csv")
    return df