import joblib
import pandas as pd

MODEL_FILE = "../models/sales_forecast_model.pkl"


def main():

    model = joblib.load(MODEL_FILE)

    features = [
        "Quantity",
        "Discount",
        "Ship_Days",
        "Year",
        "Month",
        "Quarter"
    ]

    importance = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    print(importance)


if __name__ == "__main__":
    main()