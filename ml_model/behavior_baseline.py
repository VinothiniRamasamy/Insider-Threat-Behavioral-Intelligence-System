import pandas as pd

def behavior_baseline():

    print("=" * 60)
    print("BEHAVIOR BASELINE")
    print("=" * 60)

    # --------------------------------------------------
    # Load Daily Feature Dataset
    # --------------------------------------------------

    daily = pd.read_csv("../dataset/daily_user_features.csv")

    print("\nDaily Feature Dataset Loaded")
    print("Shape :", daily.shape)

    # --------------------------------------------------
    # Features Used For Baseline
    # --------------------------------------------------

    feature_columns = [

        "logon_count",
        "off_hours_logons",
        "distinct_pcs",

        "usb_connects",
        "off_hours_usb",

        "files_copied_to_usb",
        "sensitive_files_to_usb",

        "total_emails_sent",
        "external_emails_sent",
        "total_attachments",
        "total_email_size",

        "http_requests",
        "cloud_job_visits"

    ]

    # --------------------------------------------------
    # Create User Behavior Baseline
    # --------------------------------------------------

    baseline = (
        daily.groupby("user")[feature_columns]
        .mean()
        .reset_index()
    )

    print("\nBehavior Baseline Created")
    print(baseline.head())

    print("\nColumns")
    print(baseline.columns.tolist())

    print("\nBaseline Shape :", baseline.shape)

    # --------------------------------------------------
    # Save Baseline
    # --------------------------------------------------

    baseline.to_csv(
        "../dataset/behavior_baseline.csv",
        index=False
    )

    print("\nBehavior Baseline Saved Successfully")
    print("../dataset/behavior_baseline.csv")

    return {
        "status": "success",
        "message": "Behavior Baseline Completed"
    }


if __name__ == "__main__":
    behavior_baseline()