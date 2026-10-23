import numpy as np
import pandas as pd
import joblib
from pathlib import Path
from sklearn.metrics import pairwise_distances

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data" / "raw" / "nutrition_categorized_v2.csv")

scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")
knn = joblib.load(BASE_DIR / "models" / "knn_model.pkl")

CATEGORIES = ["Semua"] + sorted(df["category_v2"].dropna().unique().tolist())


def recommend_food(calories, proteins, fat, carbohydrate, n=5, category="Semua"):
    input_nutritions = pd.DataFrame(
        [[calories, proteins, fat, carbohydrate]],
        columns=["calories", "proteins", "fat", "carbohydrate"],
    )

    input_scaled = scaler.transform(input_nutritions)

    if category != "Semua":
        candidate_data = df[df["category_v2"] == category].copy()
    else:
        candidate_data = df.copy()

    if candidate_data.empty:
        return pd.DataFrame(
            columns=[
                "id",
                "name",
                "calories",
                "proteins",
                "fat",
                "carbohydrate",
                "image",
                "category_v2",
                "distance",
            ]
        )

    n = min(n, len(candidate_data))

    candidate_features = candidate_data[
        ["calories", "proteins", "fat", "carbohydrate"]
    ]

    candidate_scaled = scaler.transform(candidate_features)

    distances = pairwise_distances(
        input_scaled,
        candidate_scaled,
        metric="euclidean",
    )[0]

    nearest_indices = np.argsort(distances)[:n]

    recommendations = candidate_data.iloc[nearest_indices].copy()
    recommendations["distance"] = distances[nearest_indices]

    result = recommendations[
        [
            "id",
            "name",
            "calories",
            "proteins",
            "fat",
            "carbohydrate",
            "image",
            "category_v2",
            "distance",
        ]
    ]

    return result.reset_index(drop=True)
