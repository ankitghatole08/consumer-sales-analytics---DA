import pandas as pd

INPUT_FILE = "../data/processed/superstore_cleaned.csv"

OUTPUT_FILE = "../data/processed/superstore_features.csv"


def create_features(df):

    df["Year"] = df["Order_Date"].dt.year
    df["Month"] = df["Order_Date"].dt.month
    df["Month_Name"] = df["Order_Date"].dt.month_name()

    df["Quarter"] = df["Order_Date"].dt.quarter

    df["Day"] = df["Order_Date"].dt.day

    df["Weekday"] = df["Order_Date"].dt.day_name()

    df["Ship_Days"] = (
        df["Ship_Date"] - df["Order_Date"]
    ).dt.days

    return df


def main():

    df = pd.read_csv(
        INPUT_FILE,
        parse_dates=["Order_Date", "Ship_Date"]
    )

    df = create_features(df)

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(df.shape)


if __name__ == "__main__":
    main()