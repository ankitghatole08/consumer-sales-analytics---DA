import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor


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

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=500,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    print(f"MAE: {mae:.2f}")

    joblib.dump(
        model,
        MODEL_FILE
    )

    print("Model saved")


if __name__ == "__main__":
    main()