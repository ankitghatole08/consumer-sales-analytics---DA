import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "../data/processed/superstore_features.csv"


df = pd.read_csv(INPUT_FILE)

# Monthly Sales Trend

monthly_sales = (
    df.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Period"] = (
    monthly_sales["Year"].astype(str)
    + "-"
    + monthly_sales["Month"].astype(str)
)

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales["Period"], monthly_sales["Sales"])
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("../reports/monthly_sales_trend.png")
plt.close()

# Category Sales

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.tight_layout()
plt.savefig("../reports/category_sales.png")
plt.close()

# Region Sales

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.tight_layout()
plt.savefig("../reports/region_sales.png")
plt.close()

print("Charts created")