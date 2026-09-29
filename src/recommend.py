import numpy as np
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data" / "raw" / "nutrition.csv")

scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")
knn = joblib.load(BASE_DIR / "models" / "knn_model.pkl")

def recommend_food(calories, proteins, fat, carbohydrate, n=5):
    
    input_nutritions = pd.DataFrame(
        [[calories, proteins, fat, carbohydrate]],
        columns =[
            "calories",
            "proteins",
            "fat",
            "carbohydrate"
        ]
)
    
    input_scaled = scaler.transform(input_nutritions)
    
    distances, indices = knn.kneighbors(
        input_scaled,
        n_neighbors=n
    )
    
    recommendations = df.iloc[indices[0]].copy()
    
    recommendations["distance"] = distances[0]
    
    result = recommendations[
        [
            'id',
            'name',
            'calories',
            'proteins',
            'fat',
            'carbohydrate',
            'image',
            'distance'
        ]
    ]
    
    return result