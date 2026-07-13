import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import joblib

print("Loading Feature Dataset...")

# ---------------------------------
# Load Dataset
# ---------------------------------

data = pd.read_csv("../dataset/final_features.csv")

print("Dataset Loaded Successfully!")
print(data.head())

# ---------------------------------
# Features & Label
# ---------------------------------

X = data.drop(["user", "label"], axis=1)
y = data["label"]

print("\nFeature Columns:")
print(X.columns.tolist())

print("\nLabel Distribution:")
print(y.value_counts())

# ---------------------------------
# Train Test Split
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

# ---------------------------------
# Random Forest Model
# ---------------------------------

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Training Completed!")

# ---------------------------------
# Prediction
# ---------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(f"\nAccuracy : {accuracy*100:.2f}%")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# ---------------------------------
# Feature Importance
# ---------------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Important Features")
print(importance)

# ---------------------------------
# Save Model
# ---------------------------------

joblib.dump(
    model,
    "../dataset/insider_threat_model.pkl"
)

print("\nModel Saved Successfully!")
print("Saved Path : ../dataset/insider_threat_model.pkl")