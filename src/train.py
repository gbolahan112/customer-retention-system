from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd
import joblib


def train_model(df):

    # --------------------------------
    # Features
    # --------------------------------
    X = df[
        [
            "Bedrooms",
            "Neighboorhood",
            "Property_Type",
            "Furnished",
            "Serviced",
            "Luxury",
            "New_Building"
        ]
    ]

    # Target
    y = df["Price"]

    # --------------------------------
    # Encode categorical variables
    # --------------------------------
    X = pd.get_dummies(X, drop_first=True)

    # Save columns
    joblib.dump(X.columns.tolist(), "models/rent_columns.pkl")

    # --------------------------------
    # Train-test split
    # --------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --------------------------------
    # Random Forest Model
    # --------------------------------
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        max_depth=20
    )

    # Train model
    model.fit(X_train, y_train)

    # --------------------------------
    # Predictions
    # --------------------------------
    y_pred = model.predict(X_test)

    # --------------------------------
    # Evaluation
    # --------------------------------
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n==============================")
    print("RANDOM FOREST PERFORMANCE")
    print("==============================")

    print(f"Mean Absolute Error: {mae:,.2f}")
    print(f"R2 Score: {r2:.2f}")

    # --------------------------------
    # Save model
    # --------------------------------
    joblib.dump(model, "models/rent_model.pkl")
    joblib.dump(X.columns.tolist(), "models/rent_columns.pkl")

    return model