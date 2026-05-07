from src.data import load_data
from src.features import preprocess_data
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

if __name__ == "__main__":
    main()