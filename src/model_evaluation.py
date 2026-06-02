import pandas as pd
import joblib

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

INPUT_FILE = "../data/processed/superstore_features.csv"

MODEL_FILE = "../models/sales_forecast_model.pkl"


def prepare_data(df):

    y = df["Sales"]

    drop_columns = [
        "Sales",
        "Order_ID",
        "Customer_ID",
        "Customer_Name",
        "Order_Date",
        "Ship_Date"
    ]

    X = df.drop(
        columns=drop_columns,
        errors="ignore"
    )

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y


def main():

    df = pd.read_csv(INPUT_FILE)

    X, y = prepare_data(df)

    model = joblib.load(MODEL_FILE)

    predictions = model.predict(X)

    mae = mean_absolute_error(
        y,
        predictions
    )

    rmse = (
        mean_squared_error(
            y,
            predictions
        ) ** 0.5
    )

    r2 = r2_score(
        y,
        predictions
    )

    print("\nMODEL PERFORMANCE\n")

    print(f"MAE : {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2  : {r2:.4f}")


if __name__ == "__main__":
    main()