import pandas as pd

FILE_PATH = "../data/processed/superstore_cleaned.csv"


def validate(df):

    checks = []

    checks.append(
        ("Sales Negative", (df["Sales"] < 0).sum())
    )

    checks.append(
        ("Null Sales", df["Sales"].isnull().sum())
    )

    checks.append(
        ("Null Order Date", df["Order_Date"].isnull().sum())
    )

    checks.append(
        ("Null Customer", df["Customer_ID"].isnull().sum())
    )

    for check, value in checks:
        print(f"{check}: {value}")

    print("Validation Completed")


def main():

    df = pd.read_csv(FILE_PATH)

    validate(df)


if __name__ == "__main__":
    main()