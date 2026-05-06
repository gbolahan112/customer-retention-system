from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib


def train_model(df):
    # Split features and target
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Pipeline: scaling + model
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("logreg", LogisticRegression(max_iter=2000, class_weight="balanced"))
    ])

    # Train model
    model.fit(X_train, y_train)

    # ✅ Save model
    joblib.dump(model, "models/churn_model.pkl")

    # ✅ Save feature columns (VERY IMPORTANT)
    joblib.dump(X.columns.tolist(), "models/churn_columns.pkl")

    return model, X_test, y_test