import pandas as pd

# Load datasets
print("Loading datasets...")

http = pd.read_csv("../dataset/http.csv", nrows=500000)
logon = pd.read_csv("../dataset/logon.csv", nrows=500000)
device = pd.read_csv("../dataset/device.csv", nrows=400000)
file = pd.read_csv("../dataset/file.csv", nrows=400000)
email = pd.read_csv("../dataset/email.csv", nrows=500000)
insiders = pd.read_csv("../dataset/insiders.csv")

print("Datasets Loaded Successfully!")

# Insider Users
insider_users = set(insiders["user"])

# -------------------------------
# HTTP Features
# -------------------------------
http["date"] = pd.to_datetime(http["date"])
http["hour"] = http["date"].dt.hour
http["after_hours"] = (
    (http["hour"] < 8) | (http["hour"] > 18)
).astype(int)

http_feature = (
    http.groupby("user")
    .agg(
        http_count=("id", "count"),
        after_hours=("after_hours", "sum"),
        unique_pc=("pc", "nunique"),
        unique_url=("url", "nunique")
    )
    .reset_index()
)

# -------------------------------
# LOGON
# -------------------------------
logon_feature = (
    logon.groupby("user")
    .agg(
        logon_count=("id", "count")
    )
    .reset_index()
)

# -------------------------------
# DEVICE
# -------------------------------
device_feature = (
    device.groupby("user")
    .agg(
        device_count=("id", "count"),
        device_activity=("activity", "nunique")
    )
    .reset_index()
)

# -------------------------------
# FILE
# -------------------------------
file_feature = (
    file.groupby("user")
    .agg(
        file_count=("id", "count"),
        unique_files=("filename", "nunique")
    )
    .reset_index()
)

# -------------------------------
# EMAIL
# -------------------------------
email_feature = (
    email.groupby("user")
    .agg(
        email_count=("id", "count"),
        total_attachment=("attachments", "sum"),
        unique_receivers=("to", "nunique")
    )
    .reset_index()
)

# -------------------------------
# Merge All
# -------------------------------
df = http_feature

df = df.merge(logon_feature, on="user", how="left")
df = df.merge(device_feature, on="user", how="left")
df = df.merge(file_feature, on="user", how="left")
df = df.merge(email_feature, on="user", how="left")

df.fillna(0, inplace=True)

# -------------------------------
# Label
# -------------------------------
df["label"] = df["user"].isin(insider_users).astype(int)

print(df.head())

print(df["label"].value_counts())

df.to_csv("behavior_dataset.csv", index=False)

print("behavior_dataset.csv saved successfully.")