import pandas as pd

INPUT_FILE = "../data/raw/superstore.csv"

OUTPUT_FILE = "../data/processed/superstore_cleaned.csv"


def load_data():
    return pd.read_csv(INPUT_FILE, encoding="latin1")


def clean_data(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

    df = df.drop_duplicates()

    df = df.dropna(subset=["Sales"])

    return df


def save_data(df):
    df.to_csv(OUTPUT_FILE, index=False)


def main():

    df = load_data()

    df = clean_data(df)

    save_data(df)

    print(df.shape)


if __name__ == "__main__":
    main()