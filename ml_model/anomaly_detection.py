import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest


def anomaly_detection():

    print("=" * 60)
    print("ANOMALY DETECTION")
    print("=" * 60)

    # --------------------------------------------------
    # Load Dataset
    # --------------------------------------------------

    data = pd.read_csv("../dataset/behavior_deviation.csv")

    print("\nDataset Loaded Successfully")
    print("Shape :", data.shape)

    # --------------------------------------------------
    # Features
    # --------------------------------------------------

    feature_columns = [

        "logon_count_deviation",
        "off_hours_logons_deviation",
        "distinct_pcs_deviation",

        "usb_connects_deviation",
        "off_hours_usb_deviation",

        "files_copied_to_usb_deviation",
        "sensitive_files_to_usb_deviation",

        "total_emails_sent_deviation",
        "external_emails_sent_deviation",

        "total_attachments_deviation",
        "total_email_size_deviation",

        "http_requests_deviation",
        "cloud_job_visits_deviation"

    ]

    X = data[feature_columns]

    print("\nSelected Features")
    print(X.head())

    # --------------------------------------------------
    # Train Isolation Forest
    # --------------------------------------------------

    model = IsolationForest(

        contamination=0.02,
        random_state=42,
        n_estimators=200

    )

    model.fit(X)

    print("\nIsolation Forest Model Trained Successfully")

    # --------------------------------------------------
    # Predict
    # --------------------------------------------------

    prediction = model.predict(X)

    data["anomaly"] = prediction

    data["anomaly"] = data["anomaly"].map({

        1: "Normal",
        -1: "Anomaly"

    })

    data["anomaly_score"] = -model.decision_function(X)

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    print("\nPrediction Summary")
    print(data["anomaly"].value_counts())

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    data.to_csv(
        "../dataset/anomaly_results.csv",
        index=False
    )

    joblib.dump(
        model,
        "../dataset/isolation_forest_model.pkl"
    )

    print("\nAnomaly Results Saved Successfully")
    print("../dataset/anomaly_results.csv")

    print("\nIsolation Forest Model Saved Successfully")
    print("../dataset/isolation_forest_model.pkl")

    return {
        "status": "success",
        "message": "Anomaly Detection Completed"
    }


if __name__ == "__main__":
    anomaly_detection()