from src.monitoring.data_drift import run_data_drift_check
from src.alerts.alert_manager import send_alert
from src.retraining.retrain_model import retrain_model

def run_monitoring_pipeline():
    drift = run_data_drift_check()

    if drift:
        send_alert("⚠️ Data drift detected! Retraining model...")
        model_path = retrain_model()
        print(f"Model retrained and saved: {model_path}")
    else:
        print("✅ No drift detected. Model is stable.")


if __name__ == "__main__":
    run_monitoring_pipeline()