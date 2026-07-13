import pandas as pd
import joblib

print("Loading Model...")

model = joblib.load("../dataset/insider_threat_model.pkl")

print("Loading Dataset...")

data = pd.read_csv("../dataset/final_features.csv")

X = data.drop(["user", "label"], axis=1)
y = data["label"]

print("\nFeature Order Used for Training:")
print(X.columns.tolist())

pred = model.predict(X)

print("\n==========================")
print("MODEL CHECK")
print("==========================")

print("Actual Insider Users    :", sum(y == 1))
print("Predicted Insider Users :", sum(pred == 1))

correct = (pred == y).sum()
print("Correct Predictions     :", correct)
print("Total Records           :", len(y))

print("\nSample Insider Records:")
print(data[data["label"] == 1].head())

print("\nPrediction Completed Successfully!")

print("\n\nTesting with Actual Insider Record...")

sample = data[data["label"] == 1].iloc[[0]]

X_sample = sample.drop(["user", "label"], axis=1)

print(X_sample)

prediction = model.predict(X_sample)[0]
prob = model.predict_proba(X_sample)[0]

print("\nPrediction :", prediction)
print("Confidence :", max(prob) * 100)