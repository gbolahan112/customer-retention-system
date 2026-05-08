from src.data import load_data
from src.features import preprocess_data
from src.train import train_model
from src.evaluate import evaluate_model


def main():

    # Load dataset
    df = load_data()

    # Preprocess dataset
    df = preprocess_data(df)

    # Show encoded features
    print(df.columns)

    # Train model
    model, X_test, y_test = train_model(df)

    # Evaluate model
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()