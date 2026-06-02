import pandas as pd
import sqlite3

INPUT_FILE = "../data/processed/superstore_features.csv"

DATABASE = "../sql/superstore.db"


df = pd.read_csv(INPUT_FILE)

conn = sqlite3.connect(DATABASE)

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created")