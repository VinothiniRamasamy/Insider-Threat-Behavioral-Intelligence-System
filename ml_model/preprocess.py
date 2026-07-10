import pandas as pd

print("Loading datasets...")

# Read only required rows for development
http = pd.read_csv("../dataset/http.csv", nrows=500000)
logon = pd.read_csv("../dataset/logon.csv", nrows=500000)
device = pd.read_csv("../dataset/device.csv", nrows=400000)
file = pd.read_csv("../dataset/file.csv", nrows=400000)
email = pd.read_csv("../dataset/email.csv", nrows=500000)
insiders = pd.read_csv("../dataset/insiders.csv")

print("Datasets Loaded Successfully!")


# -----------------------------
# Date Conversion
# -----------------------------

http["date"] = pd.to_datetime(http["date"])
logon["date"] = pd.to_datetime(logon["date"])
device["date"] = pd.to_datetime(device["date"])
file["date"] = pd.to_datetime(file["date"])
email["date"] = pd.to_datetime(email["date"])


insiders["start"] = pd.to_datetime(
    insiders["start"],
    format="mixed",
    errors="coerce"
)

insiders["end"] = pd.to_datetime(
    insiders["end"],
    format="mixed",
    errors="coerce"
)


# Remove invalid insider records

insiders = insiders.dropna(subset=["start", "end"])


print("\nSample Insider Records:")
print(insiders.head())


# -----------------------------
# Insider User Label Creation
# -----------------------------

# Get insider user list

insider_users = insiders["user"].unique()


print("\nTotal Insider Users:", len(insider_users))
print("Sample Insider Users:")
print(insider_users[:10])


# Add label column
# 1 = Insider
# 0 = Normal User

http["label"] = http["user"].isin(insider_users).astype(int)

logon["label"] = logon["user"].isin(insider_users).astype(int)

device["label"] = device["user"].isin(insider_users).astype(int)

file["label"] = file["user"].isin(insider_users).astype(int)

email["label"] = email["user"].isin(insider_users).astype(int)



# -----------------------------
# Check Labels
# -----------------------------

print("\nHTTP Label Distribution")
print(http["label"].value_counts())


print("\nLogon Label Distribution")
print(logon["label"].value_counts())


print("\nDevice Label Distribution")
print(device["label"].value_counts())


print("\nFile Label Distribution")
print(file["label"].value_counts())


print("\nEmail Label Distribution")
print(email["label"].value_counts())


print("\nPreprocessing Completed Successfully!")