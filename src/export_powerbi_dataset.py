import pandas as pd

INPUT_FILE = "../data/processed/superstore_features.csv"

OUTPUT_FILE = "../dashboard/powerbi_dataset.csv"


df = pd.read_csv(INPUT_FILE)

columns = [
    "Order_ID",
    "Order_Date",
    "Sales",
    "Profit",
    "Quantity",
    "Discount",
    "Category",
    "Sub_Category",
    "Region",
    "State",
    "Segment",
    "Customer_ID",
    "Customer_Name",
    "Ship_Days",
    "Year",
    "Month",
    "Quarter"
]

df[columns].to_csv(
    OUTPUT_FILE,
    index=False
)

print("Power BI dataset exported")