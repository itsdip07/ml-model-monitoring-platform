import pandas as pd
from datetime import datetime
import os

LOG_FILE = "data/predictions_log.csv"

def log_prediction(features: dict, prediction: int, latency_ms: float):
    log = {
        **features,
        "prediction": prediction,
        "latency_ms": latency_ms,
        "timestamp": datetime.utcnow()
    }

    df = pd.DataFrame([log])

    if not os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, index=False)
    else:
        df.to_csv(LOG_FILE, mode="a", header=False, index=False)
