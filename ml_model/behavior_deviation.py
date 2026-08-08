import pandas as pd

def behavior_deviation():

    print("=" * 60)
    print("BEHAVIOR DEVIATION ANALYSIS")
    print("=" * 60)

    # --------------------------------------------------
    # Load Datasets
    # --------------------------------------------------

    daily = pd.read_csv("../dataset/daily_user_features.csv")
    baseline = pd.read_csv("../dataset/behavior_baseline.csv")

    print("\nDatasets Loaded Successfully")
    print("Daily Dataset :", daily.shape)
    print("Baseline      :", baseline.shape)

    # --------------------------------------------------
    # Merge Daily + Baseline
    # --------------------------------------------------

    data = daily.merge(
        baseline,
        on="user",
        suffixes=("", "_baseline")
    )

    print("\nMerged Dataset :", data.shape)

    # --------------------------------------------------
    # Features
    # --------------------------------------------------

    features = [

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
    # Calculate Deviations
    # --------------------------------------------------

    for feature in features:

        data[f"{feature}_deviation"] = (

            data[feature] -
            data[f"{feature}_baseline"]

        )

    # --------------------------------------------------
    # Display Sample
    # --------------------------------------------------

    print("\nBehavior Deviation Sample")

    print(

        data[
            [
                "user",
                "activity_date",
                "logon_count",
                "logon_count_baseline",
                "logon_count_deviation"
            ]
        ].head()

    )

    print("\nColumns")
    print(data.columns.tolist())

    print("\nShape :", data.shape)

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    data.to_csv(
        "../dataset/behavior_deviation.csv",
        index=False
    )

    print("\nBehavior Deviation Dataset Saved Successfully")
    print("../dataset/behavior_deviation.csv")

    return {
        "status": "success",
        "message": "Behavior Deviation Completed"
    }


if __name__ == "__main__":
    behavior_deviation()