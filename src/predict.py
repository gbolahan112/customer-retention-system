import joblib
import pandas as pd


<<<<<<< HEAD
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
=======
def load_model():

    model = joblib.load("models/rent_model.pkl")

    columns = joblib.load("models/rent_columns.pkl")

    return model, columns


def make_prediction(model, columns, input_data):

    # Convert to DataFrame
    df = pd.DataFrame([input_data])

    # Encode categorical variables
    df = pd.get_dummies(df)
>>>>>>> a53356297f8ef74e1d22691e3d1f58a4f1734fcf

    # Add missing columns
    for col in columns:
        if col not in df.columns:
            df[col] = 0

<<<<<<< HEAD
    # Reorder columns
=======
    # Ensure correct order
>>>>>>> a53356297f8ef74e1d22691e3d1f58a4f1734fcf
    df = df[columns]

    # Predict
    prediction = model.predict(df)[0]
<<<<<<< HEAD
    probability = model.predict_proba(df)[0][1]

    return int(prediction), float(probability)
=======

    return prediction
>>>>>>> a53356297f8ef74e1d22691e3d1f58a4f1734fcf
