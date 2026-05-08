from src.data import load_data
from src.features import preprocess_data
<<<<<<< HEAD
from src.train import train_model
from src.evaluate import evaluate_model


def main():
    df = load_data()
    df = preprocess_data(df)

    print(df.columns)  # 👈 This will show your encoded features

    model, X_test, y_test = train_model(df)
    evaluate_model(model, X_test, y_test)

=======
from src.evaluate import analyze_data
from src.train import train_model


def main():

    # Load dataset
    df = load_data()

    # Clean dataset
    df = preprocess_data(df)

    # Analyze dataset
    analyze_data(df)

    # Train model
    train_model(df)
    print(df["Neighboorhood"].unique())
>>>>>>> a53356297f8ef74e1d22691e3d1f58a4f1734fcf

if __name__ == "__main__":
    main()