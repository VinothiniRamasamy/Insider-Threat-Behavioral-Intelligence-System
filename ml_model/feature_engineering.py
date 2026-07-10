import pandas as pd

print("Loading preprocessed datasets...")


# Load datasets
http = pd.read_csv("../dataset/http.csv", nrows=500000)
logon = pd.read_csv("../dataset/logon.csv", nrows=500000)
device = pd.read_csv("../dataset/device.csv", nrows=400000)
file = pd.read_csv("../dataset/file.csv", nrows=400000)
email = pd.read_csv("../dataset/email.csv", nrows=500000)
insiders = pd.read_csv("../dataset/insiders.csv")


# Get insider users

insider_users = insiders["user"].unique()


print("Creating Features...")


# -------------------------
# Logon Features
# -------------------------

logon_features = logon.groupby("user").size().reset_index(name="login_count")


# -------------------------
# Device Features
# -------------------------

device_features = device.groupby("user").size().reset_index(name="device_usage_count")


# -------------------------
# File Features
# -------------------------

file_features = file.groupby("user").size().reset_index(name="file_access_count")


# -------------------------
# HTTP Features
# -------------------------

http_features = http.groupby("user").size().reset_index(name="web_visit_count")


# -------------------------
# Email Features
# -------------------------

email_features = email.groupby("user").agg(
    email_count=("id","count"),
    total_attachment=("attachments","sum")
).reset_index()



# -------------------------
# Merge all features
# -------------------------

features = logon_features

features = features.merge(device_features, on="user", how="outer")
features = features.merge(file_features, on="user", how="outer")
features = features.merge(http_features, on="user", how="outer")
features = features.merge(email_features, on="user", how="outer")


# Fill missing values

features = features.fillna(0)


# Add Label

features["label"] = features["user"].isin(insider_users).astype(int)



print("\nFinal Feature Dataset")
print(features.head())


print("\nShape:")
print(features.shape)


# Save dataset

features.to_csv("../dataset/final_features.csv", index=False)


print("\nFeature Engineering Completed Successfully!")