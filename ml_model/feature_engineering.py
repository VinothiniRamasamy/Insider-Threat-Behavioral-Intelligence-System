import pandas as pd

print("Loading datasets...")

# -----------------------------
# Load datasets
# -----------------------------

http = pd.read_csv("../dataset/http.csv", nrows=500000)
logon = pd.read_csv("../dataset/logon.csv", nrows=500000)
device = pd.read_csv("../dataset/device.csv", nrows=400000)
file = pd.read_csv("../dataset/file.csv", nrows=400000)
email = pd.read_csv("../dataset/email.csv", nrows=500000)
insiders = pd.read_csv("../dataset/insiders.csv")

# -----------------------------
# Convert date columns
# -----------------------------

http["date"] = pd.to_datetime(http["date"])
logon["date"] = pd.to_datetime(logon["date"])
device["date"] = pd.to_datetime(device["date"])
file["date"] = pd.to_datetime(file["date"])
email["date"] = pd.to_datetime(email["date"])

# -----------------------------
# Insider Users
# -----------------------------

insider_users = insiders["user"].unique()

print("Creating Features...")

# =====================================================
# HTTP FEATURES
# =====================================================

http_features = http.groupby("user").agg(
    http_count=("id", "count"),
    unique_url=("url", "nunique")
).reset_index()

# =====================================================
# LOGON FEATURES
# =====================================================

logon["hour"] = logon["date"].dt.hour

logon_features = logon.groupby("user").agg(
    logon_count=("id", "count"),
    unique_pc=("pc", "nunique"),
    after_hours=("hour", lambda x: ((x < 8) | (x > 18)).sum())
).reset_index()

# =====================================================
# DEVICE FEATURES
# =====================================================

device_features = device.groupby("user").agg(
    device_count=("pc", "nunique"),
    device_activity=("id", "count")
).reset_index()

# =====================================================
# FILE FEATURES
# =====================================================

file_features = file.groupby("user").agg(
    file_count=("id", "count"),
    unique_files=("filename", "nunique")
).reset_index()

# =====================================================
# EMAIL FEATURES
# =====================================================

email_features = email.groupby("user").agg(
    email_count=("id", "count"),
    total_attachment=("attachments", "sum"),
    unique_receivers=("to", "nunique")
).reset_index()

# Replace missing attachment values
email_features["total_attachment"] = (
    email_features["total_attachment"]
    .fillna(0)
)

# =====================================================
# MERGE ALL FEATURES
# =====================================================

features = http_features

features = features.merge(logon_features, on="user", how="outer")
features = features.merge(device_features, on="user", how="outer")
features = features.merge(file_features, on="user", how="outer")
features = features.merge(email_features, on="user", how="outer")

# =====================================================
# FILL MISSING VALUES
# =====================================================

features = features.fillna(0)

# Convert numeric columns to int

for col in features.columns:
    if col != "user":
        features[col] = features[col].astype(int)

# =====================================================
# LABEL
# =====================================================

features["label"] = features["user"].isin(insider_users).astype(int)

# =====================================================
# DISPLAY
# =====================================================

print("\nFinal Features")
print(features.head())

print("\nColumns")
print(features.columns.tolist())

print("\nShape")
print(features.shape)

print("\nLabel Distribution")
print(features["label"].value_counts())

# =====================================================
# SAVE
# =====================================================

features.to_csv("../dataset/final_features.csv", index=False)

print("\nFeature Engineering Completed Successfully!")