import joblib
import pandas as pd


def load_model():

    model = joblib.load("models/rent_model.pkl")

    columns = joblib.load("models/rent_columns.pkl")

    return model, columns


def make_prediction(model, columns, input_data):

    # Convert to DataFrame
    df = pd.DataFrame([input_data])

    # Encode categorical variables
    df = pd.get_dummies(df)

    # Add missing columns
    for col in columns:
        if col not in df.columns:
            df[col] = 0

    # Ensure correct order
    df = df[columns]

    # Predict
    prediction = model.predict(df)[0]

    return prediction