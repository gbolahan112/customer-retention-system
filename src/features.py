import pandas as pd

def preprocess_data(df):
    print(df.columns)
    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Drop missing values
    df = df.dropna()

    # Drop unnecessary column
    df = df.drop("customerID", axis=1)

    # Encode target
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Convert TotalCharges to numeric (important fix)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Drop missing values
    df = df.dropna()

    # One-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    # Convert bool to int
    df = df.astype(int)

    return df