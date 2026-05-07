import pandas as pd


def preprocess_data(df):

    # --------------------------------
    # Remove useless columns
    # --------------------------------
    df = df.drop(["Unnamed: 0", "Pid"], axis=1)

    # --------------------------------
    # Remove missing values
    # --------------------------------
    df = df.dropna()

    # --------------------------------
    # Remove duplicates
    # --------------------------------
    df = df.drop_duplicates()

    # --------------------------------
    # Extract Bedrooms
    # --------------------------------
    df["Bedrooms"] = df["Property_name"].str.extract(r'(\d+)\s*bedroom')

    # Convert to numeric
    df["Bedrooms"] = pd.to_numeric(df["Bedrooms"], errors="coerce")

# Remove unrealistic bedroom values
    df = df[(df["Bedrooms"] >= 1) & (df["Bedrooms"] <= 10)]

# Fill missing values
    df["Bedrooms"] = df["Bedrooms"].fillna(1)

    # --------------------------------
    # Extract Property Type
    # --------------------------------
    df["Property_Type"] = df["Property_name"].apply(
        lambda x: x.split("for rent")[0].strip()
    )

    # --------------------------------
    # Furnished Feature
    # --------------------------------
    df["Furnished"] = df["Property_name"].str.contains(
        "furnished", case=False, na=False
    ).astype(int)

    # --------------------------------
    # Serviced Feature
    # --------------------------------
    df["Serviced"] = df["Property_name"].str.contains(
        "serviced", case=False, na=False
    ).astype(int)

    # --------------------------------
    # Luxury Feature
    # --------------------------------
    luxury_keywords = [
        "luxury",
        "executive",
        "premium",
        "exclusive"
    ]

    df["Luxury"] = df["Property_name"].apply(
        lambda x: int(any(word in x.lower() for word in luxury_keywords))
    )

    # --------------------------------
    # New Building Feature
    # --------------------------------
    df["New_Building"] = df["Property_name"].str.contains(
        "new", case=False, na=False
    ).astype(int)

    return df