import pandas as pd

def feature_engineering():

    print("=" * 60)
    print("FEATURE ENGINEERING")
    print("=" * 60)

    # --------------------------------------------------
    # Load Cleaned Datasets
    # --------------------------------------------------

    http = pd.read_csv("../dataset/http_clean.csv")
    logon = pd.read_csv("../dataset/logon_clean.csv")
    device = pd.read_csv("../dataset/device_clean.csv")
    file = pd.read_csv("../dataset/file_clean.csv")
    email = pd.read_csv("../dataset/email_clean.csv")

    print("\nDatasets Loaded Successfully")

    # --------------------------------------------------
    # Convert Date Columns
    # --------------------------------------------------

    http["date"] = pd.to_datetime(http["date"])
    logon["date"] = pd.to_datetime(logon["date"])
    device["date"] = pd.to_datetime(device["date"])
    file["date"] = pd.to_datetime(file["date"])
    email["date"] = pd.to_datetime(email["date"])

    # Activity Date

    http["activity_date"] = http["date"].dt.date
    logon["activity_date"] = logon["date"].dt.date
    device["activity_date"] = device["date"].dt.date
    file["activity_date"] = file["date"].dt.date
    email["activity_date"] = email["date"].dt.date

    # ==================================================
    # HTTP FEATURES
    # ==================================================

    cloud_sites = [
        "dropbox",
        "drive.google",
        "onedrive",
        "box",
        "icloud"
    ]

    http["cloud"] = http["url"].str.lower().str.contains(
        "|".join(cloud_sites),
        na=False
    )

    http_features = http.groupby(
        ["user", "activity_date"]
    ).agg(
        http_requests=("url", "count"),
        cloud_job_visits=("cloud", "sum")
    ).reset_index()

    # ==================================================
    # LOGON FEATURES
    # ==================================================

    logon["hour"] = logon["date"].dt.hour

    logon["off_hours"] = (
        (logon["hour"] < 8) |
        (logon["hour"] > 18)
    )

    logon_features = logon.groupby(
        ["user", "activity_date"]
    ).agg(
        logon_count=("activity", lambda x: (x == "Logon").sum()),
        off_hours_logons=("off_hours", "sum"),
        distinct_pcs=("pc", "nunique")
    ).reset_index()

    # ==================================================
    # DEVICE FEATURES
    # ==================================================

    device["hour"] = device["date"].dt.hour

    device["off_hours"] = (
        (device["hour"] < 8) |
        (device["hour"] > 18)
    )

    device_features = device.groupby(
        ["user", "activity_date"]
    ).agg(
        usb_connects=("activity", lambda x: (x == "Connect").sum()),
        off_hours_usb=("off_hours", "sum")
    ).reset_index()

    # ==================================================
    # FILE FEATURES
    # ==================================================

    keywords = [
        "secret",
        "confidential",
        "salary",
        "finance",
        "hr"
    ]

    file["sensitive"] = file["filename"].astype(str).str.lower().str.contains(
        "|".join(keywords),
        na=False
    )

    file_features = file.groupby(
        ["user", "activity_date"]
    ).agg(
        files_copied_to_usb=("filename", "count"),
        sensitive_files_to_usb=("sensitive", "sum")
    ).reset_index()

    # ==================================================
    # EMAIL FEATURES
    # ==================================================

    email["external"] = ~email["to"].astype(str).str.contains(
        "@dtaa.com",
        case=False,
        na=False
    )

    email_features = email.groupby(
        ["user", "activity_date"]
    ).agg(
        total_emails_sent=("to", "count"),
        external_emails_sent=("external", "sum"),
        total_attachments=("attachments", "sum"),
        total_email_size=("size", "sum")
    ).reset_index()

    # ==================================================
    # MERGE EVERYTHING
    # ==================================================

    daily = logon_features

    daily = daily.merge(
        device_features,
        on=["user", "activity_date"],
        how="outer"
    )

    daily = daily.merge(
        file_features,
        on=["user", "activity_date"],
        how="outer"
    )

    daily = daily.merge(
        email_features,
        on=["user", "activity_date"],
        how="outer"
    )

    daily = daily.merge(
        http_features,
        on=["user", "activity_date"],
        how="outer"
    )

    daily.fillna(0, inplace=True)

    # ==================================================
    # SAVE
    # ==================================================

    print("\nDaily Feature Dataset")
    print(daily.head())

    print("\nColumns")
    print(daily.columns.tolist())

    print("\nShape :", daily.shape)

    daily.to_csv(
        "../dataset/daily_user_features.csv",
        index=False
    )

    print("\nFeature Dataset Saved Successfully")
    print("../dataset/daily_user_features.csv")

    return {
        "status": "success"
    }


if __name__ == "__main__":
    feature_engineering()