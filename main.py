from src.data import load_data
from src.features import preprocess_data
from src.train import train_model
from src.evaluate import evaluate_model


def main():
    df = load_data()
    df = preprocess_data(df)

    print(df.columns)  # 👈 This will show your encoded features

    model, X_test, y_test = train_model(df)
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()