import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------
# Load Dataset
# -----------------------

df = pd.read_csv("behavior_dataset.csv")

print("Behavior Dataset Loaded Successfully")
print(df.shape)

# -----------------------
# Features
# -----------------------

features = [
    "http_count",
    "after_hours",
    "unique_pc",
    "unique_url",
    "logon_count",
    "device_count",
    "device_activity",
    "file_count",
    "unique_files",
    "email_count",
    "total_attachment",
    "unique_receivers"
]

X = df[features]
y = df["label"]

print("\nFeatures Used:")
print(features)

# -----------------------
# Train Test Split
# -----------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# -----------------------
# Model
# -----------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("\nModel Training Completed!")

# -----------------------
# Prediction
# -----------------------

y_pred = model.predict(X_test)

print("\nAccuracy:",
      round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# -----------------------
# Save Model
# -----------------------

joblib.dump(model, "model.pkl")

print("\nmodel.pkl Saved Successfully!")