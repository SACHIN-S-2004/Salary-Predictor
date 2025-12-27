from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import pickle
import pandas as pd

df = pd.read_csv("Salary Data.csv")
X = df.drop("Salary", axis=1)
y = df["Salary"]

categorical_cols = ["Gender", "Education Level", "Job Title"]
numerical_cols = ["Age","Years of Experience"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

rf_model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=300,
            random_state=42
        ))
    ]
)

rf_model.fit(X, y)

with open("salaryPredict_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)

print("Model trained and saved!")
