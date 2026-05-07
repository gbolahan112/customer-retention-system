import pandas as pd


def analyze_data(df):

    print("\n==============================")
    print("TOP 10 MOST EXPENSIVE AREAS")
    print("==============================")

    expensive_areas = (
        df.groupby("Neighboorhood")["Price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    print(expensive_areas)

    print("\n==============================")
    print("AVERAGE RENT BY BEDROOMS")
    print("==============================")

    bedroom_prices = (
        df.groupby("Bedrooms")["Price"]
        .mean()
        .sort_values()
    )

    print(bedroom_prices)

    print("\n==============================")
    print("MOST COMMON PROPERTY TYPES")
    print("==============================")

    property_types = df["Property_Type"].value_counts().head(10)

    print(property_types)