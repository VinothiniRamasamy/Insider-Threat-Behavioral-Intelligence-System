import pandas as pd

# ----------------------------------
# Load Dataset
# ----------------------------------

http = pd.read_csv("../dataset/http.csv", nrows=100000)
logon = pd.read_csv("../dataset/logon.csv", nrows=100000)
insiders = pd.read_csv("../dataset/insiders.csv")

print("Datasets Loaded Successfully\n")

print("HTTP Shape:", http.shape)
print("Logon Shape:", logon.shape)
print("Insiders Shape:", insiders.shape)

# ----------------------------------
# Convert Date Columns
# ----------------------------------

http["date"] = pd.to_datetime(http["date"], errors="coerce")
logon["date"] = pd.to_datetime(logon["date"], errors="coerce")

print("Date conversion completed.")

# ----------------------------------
# Remove Missing Values
# ----------------------------------

http.dropna(inplace=True)
logon.dropna(inplace=True)

print("Missing values removed.")

# ----------------------------------
# Remove Duplicates
# ----------------------------------

http.drop_duplicates(inplace=True)
logon.drop_duplicates(inplace=True)

print("Duplicate rows removed.")

print("\nFinal Dataset Shapes")
print("HTTP :", http.shape)
print("Logon:", logon.shape)

# ----------------------------------
# Create Insider Labels
# ----------------------------------

insider_users = insiders["user"].unique()

print("\nTotal Insider Users:", len(insider_users))
print("Sample Insider Users:", insider_users[:10])

http["label"] = http["user"].isin(insider_users).astype(int)
logon["label"] = logon["user"].isin(insider_users).astype(int)

print("\nLabels Created Successfully")

print("\nHTTP Label Count")
print(http["label"].value_counts())

print("\nLogon Label Count")
print(logon["label"].value_counts())

# ----------------------------------
# Feature Engineering
# ----------------------------------

# HTTP Features
http["hour"] = http["date"].dt.hour
http["day"] = http["date"].dt.day
http["month"] = http["date"].dt.month
http["weekday"] = http["date"].dt.dayofweek

# Logon Features
logon["hour"] = logon["date"].dt.hour
logon["day"] = logon["date"].dt.day
logon["month"] = logon["date"].dt.month
logon["weekday"] = logon["date"].dt.dayofweek

print("\nFeature Engineering Completed")

print("\nHTTP Sample")
print(http[["date", "hour", "day", "month", "weekday"]].head())

print("\nLogon Sample")
print(logon[["date", "hour", "day", "month", "weekday"]].head())

# ----------------------------------
# Additional Features
# ----------------------------------

# Office Hours (8 AM - 6 PM)
http["office_hours"] = http["hour"].between(8, 18).astype(int)
logon["office_hours"] = logon["hour"].between(8, 18).astype(int)

# Weekend
http["is_weekend"] = (http["weekday"] >= 5).astype(int)
logon["is_weekend"] = (logon["weekday"] >= 5).astype(int)

print("\nAdditional Features Created Successfully")

# ----------------------------------
# Verify Columns
# ----------------------------------

print("\nHTTP Columns:")
print(http.columns)

# ----------------------------------
# Save Processed Dataset
# ----------------------------------

http.to_csv("processed_http.csv", index=False)
logon.to_csv("processed_logon.csv", index=False)

print("\nProcessed datasets saved successfully!")