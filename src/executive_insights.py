import pandas as pd

INPUT_FILE = "../data/processed/superstore_features.csv"

OUTPUT_FILE = "../reports/executive_insights.txt"


def main():

    df = pd.read_csv(INPUT_FILE)

    total_sales = round(
        df["Sales"].sum(),
        2
    )

    total_profit = round(
        df["Profit"].sum(),
        2
    )

    best_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    best_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    most_profitable_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .idxmax()
    )

    insights = f"""
TOTAL SALES: {total_sales}

TOTAL PROFIT: {total_profit}

BEST REGION: {best_region}

TOP REVENUE CATEGORY: {best_category}

MOST PROFITABLE CATEGORY: {most_profitable_category}
"""

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(insights)

    print(insights)


if __name__ == "__main__":
    main()