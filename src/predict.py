import joblib
import pandas as pd


def load_model(model_path="models/churn_model.pkl"):
    model = joblib.load(model_path)
    columns = joblib.load("models/churn_columns.pkl")
    return model, columns


def make_prediction(model, columns, input_dict):
    """
    Prepare input, align features, and make prediction
    """

    # Convert input to DataFrame
    df = pd.DataFrame([input_dict])

    # Add missing columns
    for col in columns:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns
    df = df[columns]

    # Predict
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return int(prediction), float(probability)