from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="Iris ML API", description="Predict Iris species using a trained Random Forest model.")

MODEL_PATH = "model.joblib"
model = None

def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found. Run train.py first.")
    model = joblib.load(MODEL_PATH)

load_model()

CLASS_NAMES = ["setosa", "versicolor", "virginica"]

class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sepal_length": 5.1,
                    "sepal_width": 3.5,
                    "petal_length": 1.4,
                    "petal_width": 0.2
                }
            ]
        }
    }

class PredictionResponse(BaseModel):
    prediction: int
    species: str
    probabilities: dict

@app.get("/")
def root():
    return {"message": "ML API is running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(features: Features):
    try:
        X = np.array([[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]])
        pred = int(model.predict(X)[0])
        proba = model.predict_proba(X)[0]
        return PredictionResponse(
            prediction=pred,
            species=CLASS_NAMES[pred],
            probabilities={name: round(float(p), 4) for name, p in zip(CLASS_NAMES, proba)}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
