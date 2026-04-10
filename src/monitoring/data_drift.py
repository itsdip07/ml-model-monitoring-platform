import pandas as pd
import os
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

REFERENCE_DATA_PATH = "data/train.csv"
CURRENT_DATA_PATH = "data/predictions_log.csv"
REPORT_DIR = "data/drift_reports"

os.makedirs(REPORT_DIR, exist_ok=True)

def run_data_drift_check():
    ref_df = pd.read_csv(REFERENCE_DATA_PATH)
    curr_df = pd.read_csv(CURRENT_DATA_PATH)

    ref_features = ref_df.drop(columns=["target"])
    curr_features = curr_df[ref_features.columns]

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=ref_features, current_data=curr_features)

    # Save HTML
    report_path = os.path.join(REPORT_DIR, "data_drift_report.html")
    report.save_html(report_path)

    # Extract drift result
    result = report.as_dict()

    drift_detected = result["metrics"][0]["result"]["dataset_drift"]

    print(f"Drift Detected: {drift_detected}")
    print(f"Report saved at: {report_path}")

    return drift_detected


if __name__ == "__main__":
    run_data_drift_check()