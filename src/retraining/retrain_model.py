import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from datetime import datetime
import os

DATA_PATH = "data/predictions_log.csv"
MODEL_DIR = "models"

os.makedirs(MODEL_DIR, exist_ok=True)

def retrain_model():
    print("🔁 Retraining model...")

    df = pd.read_csv(DATA_PATH)

    # Use same structure as training
    X = df[["feature1", "feature2"]]
    y = df["prediction"]  # using prediction as pseudo-label (simulation)

    model = RandomForestClassifier()
    model.fit(X, y)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_path = os.path.join(MODEL_DIR, f"model_{timestamp}.joblib")

    joblib.dump(model, model_path)

    print(f"New model saved at: {model_path}")

    return model_path


if __name__ == "__main__":
    retrain_model()