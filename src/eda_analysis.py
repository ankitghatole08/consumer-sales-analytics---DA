import pandas as pd

INPUT_FILE = "../data/processed/superstore_features.csv"


def print_kpis(df):

    print("\n===== OVERALL KPIs =====\n")

    print(
        f"Total Sales: ${df['Sales'].sum():,.2f}"
    )

    print(
        f"Total Profit: ${df['Profit'].sum():,.2f}"
    )

    print(
        f"Total Orders: {df['Order_ID'].nunique():,}"
    )

    print(
        f"Total Customers: {df['Customer_ID'].nunique():,}"
    )


def sales_by_region(df):

    print("\n===== SALES BY REGION =====\n")

    print(
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def sales_by_category(df):

    print("\n===== SALES BY CATEGORY =====\n")

    print(
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def profit_by_category(df):

    print("\n===== PROFIT BY CATEGORY =====\n")

    print(
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )


def monthly_sales(df):

    print("\n===== MONTHLY SALES =====\n")

    print(
        df.groupby(
            ["Year", "Month"]
        )["Sales"]
        .sum()
    )


def top_customers(df):

    print("\n===== TOP 10 CUSTOMERS =====\n")

    print(
        df.groupby("Customer_Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


def main():

    df = pd.read_csv(INPUT_FILE)

    print_kpis(df)

    sales_by_region(df)

    sales_by_category(df)

    profit_by_category(df)

    monthly_sales(df)

    top_customers(df)


if __name__ == "__main__":
    main()