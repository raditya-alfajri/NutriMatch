# NutriMatch

NutriMatch is an Indonesian food recommendation system that uses **K-Nearest Neighbors (KNN)** to find foods with nutritional values that are most similar to the user's input.

The system is designed to recommend Indonesian foods based on four main nutritional features:

- Calories
- Protein
- Fat
- Carbohydrate

## Project Status

🚧 **Currently in development**

Current progress:

- [x] Dataset exploration
- [x] Data preprocessing
- [x] Missing value checking
- [x] Duplicate checking
- [x] Outlier detection
- [x] Feature scaling using StandardScaler
- [x] K-Nearest Neighbors model
- [ ] Recommendation testing
- [ ] Recommendation function
- [ ] Backend/API
- [ ] Frontend
- [ ] Final deployment

---

## How It Works

NutriMatch uses nutritional similarity to find foods that are closest to a user's nutritional input.

```text
User Input
    │
    ├── Calories
    ├── Protein
    ├── Fat
    └── Carbohydrate
          │
          ▼
    StandardScaler
          │
          ▼
    K-Nearest Neighbors
          │
          ▼
    Euclidean Distance
          │
          ▼
  Similar Indonesian Foods