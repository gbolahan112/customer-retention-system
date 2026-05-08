from sklearn.model_selection import train_test_split
<<<<<<< HEAD
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
=======
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd
>>>>>>> a53356297f8ef74e1d22691e3d1f58a4f1734fcf
import joblib


def train_model(df):
<<<<<<< HEAD
    # Split features and target
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Train-test split
=======

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
>>>>>>> a53356297f8ef74e1d22691e3d1f58a4f1734fcf
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

<<<<<<< HEAD
    # Pipeline: scaling + model
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("logreg", LogisticRegression(max_iter=2000, class_weight="balanced"))
    ])
=======
    # --------------------------------
    # Random Forest Model
    # --------------------------------
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        max_depth=20
    )
>>>>>>> a53356297f8ef74e1d22691e3d1f58a4f1734fcf

    # Train model
    model.fit(X_train, y_train)

<<<<<<< HEAD
    # ✅ Save model
    joblib.dump(model, "models/churn_model.pkl")

    # ✅ Save feature columns (VERY IMPORTANT)
    joblib.dump(X.columns.tolist(), "models/churn_columns.pkl")

    return model, X_test, y_test
=======
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
>>>>>>> a53356297f8ef74e1d22691e3d1f58a4f1734fcf
