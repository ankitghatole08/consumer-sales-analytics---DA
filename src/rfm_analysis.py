import pandas as pd

INPUT_FILE = "../data/processed/superstore_features.csv"

OUTPUT_FILE = "../data/processed/rfm_customers.csv"


def main():

    df = pd.read_csv(
        INPUT_FILE,
        parse_dates=["Order_Date"]
    )

    snapshot_date = (
        df["Order_Date"].max()
        + pd.Timedelta(days=1)
    )

    rfm = (
        df.groupby("Customer_ID")
        .agg({
            "Order_Date": lambda x: (
                snapshot_date - x.max()
            ).days,
            "Order_ID": "nunique",
            "Sales": "sum"
        })
        .reset_index()
    )

    rfm.columns = [
        "Customer_ID",
        "Recency",
        "Frequency",
        "Monetary"
    ]

    rfm["R"] = pd.qcut(
        rfm["Recency"],
        5,
        labels=[5,4,3,2,1]
    )

    rfm["F"] = pd.qcut(
        rfm["Frequency"].rank(method="first"),
        5,
        labels=[1,2,3,4,5]
    )

    rfm["M"] = pd.qcut(
        rfm["Monetary"],
        5,
        labels=[1,2,3,4,5]
    )

    rfm["RFM_Score"] = (
        rfm["R"].astype(str)
        + rfm["F"].astype(str)
        + rfm["M"].astype(str)
    )

    rfm.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(rfm.head())

    print("\nCustomers:", len(rfm))


if __name__ == "__main__":
    main()