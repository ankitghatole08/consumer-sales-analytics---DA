import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

INPUT_FILE = "../data/processed/rfm_customers.csv"

OUTPUT_FILE = "../data/processed/customer_segments.csv"


def main():

    df = pd.read_csv(INPUT_FILE)

    features = df[
        [
            "Recency",
            "Frequency",
            "Monetary"
        ]
    ]

    scaler = StandardScaler()

    scaled = scaler.fit_transform(features)

    model = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    df["Cluster"] = model.fit_predict(
        scaled
    )

    segment_names = {
        0: "High Value",
        1: "Loyal",
        2: "At Risk",
        3: "Regular"
    }

    df["Segment"] = (
        df["Cluster"]
        .map(segment_names)
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        df["Segment"]
        .value_counts()
    )


if __name__ == "__main__":
    main()