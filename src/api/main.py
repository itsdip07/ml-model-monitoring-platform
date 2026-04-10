from fastapi import FastAPI
import joblib
import pandas as pd
import time

from src.api.schema import PredictionRequest, PredictionResponse
from src.logging.prediction_logger import log_prediction

app = FastAPI(title="ML Model Monitoring API")

# Load model once at startup
model = joblib.load("model.joblib")


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    start = time.time()

    # Convert request to DataFrame
    features = request.dict()
    df = pd.DataFrame([features])

    # Model prediction
    prediction = model.predict(df)[0]

    # Latency calculation
    latency = (time.time() - start) * 1000

    # Log prediction for monitoring
    log_prediction(
        features=features,
        prediction=int(prediction),
        latency_ms=round(latency, 2)
    )

    # API response
    return PredictionResponse(
        prediction=int(prediction),
        latency_ms=round(latency, 2)
    )
