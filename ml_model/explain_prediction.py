import pandas as pd
import joblib
import shap

print("Loading Model...")

# ---------------------------------------
# Load Trained Model
# ---------------------------------------

model = joblib.load("../dataset/insider_threat_model.pkl")

# SHAP Explainer
explainer = shap.TreeExplainer(model)

print("\nEnter User Activity Details\n")

# ---------------------------------------
# User Input
# ---------------------------------------

http_count = int(input("HTTP Count: "))
unique_url = int(input("Unique URL Count: "))
logon_count = int(input("Logon Count: "))
unique_pc = int(input("Unique PC Count: "))
after_hours = int(input("After Hours Activity: "))
device_count = int(input("Device Count: "))
device_activity = int(input("Device Activity: "))
file_count = int(input("File Count: "))
unique_files = int(input("Unique Files: "))
email_count = int(input("Email Count: "))
total_attachment = int(input("Total Attachments: "))
unique_receivers = int(input("Unique Receivers: "))

# ---------------------------------------
# Create DataFrame
# ---------------------------------------

data = pd.DataFrame([{
    "http_count": http_count,
    "unique_url": unique_url,
    "logon_count": logon_count,
    "unique_pc": unique_pc,
    "after_hours": after_hours,
    "device_count": device_count,
    "device_activity": device_activity,
    "file_count": file_count,
    "unique_files": unique_files,
    "email_count": email_count,
    "total_attachment": total_attachment,
    "unique_receivers": unique_receivers
}])

# ---------------------------------------
# Prediction
# ---------------------------------------

prediction = model.predict(data)[0]
probability = model.predict_proba(data)[0]

confidence = probability[prediction] * 100

print("\n==========================")

if prediction == 1:
    print("Prediction : 🚨 Insider Threat")
    print("Risk Level : HIGH")
else:
    print("Prediction : ✅ Normal User")
    print("Risk Level : LOW")

print(f"Confidence : {confidence:.2f}%")

print("==========================")

# ---------------------------------------
# SHAP Explanation
# ---------------------------------------

print("\nTop Important Factors\n")

shap_values = explainer.shap_values(data)

if isinstance(shap_values, list):
    values = shap_values[1][0]

elif hasattr(shap_values, "values"):
    values = shap_values.values

    if len(values.shape) == 3:
        values = values[0, :, 1]
    else:
        values = values[0]

elif len(shap_values.shape) == 3:
    values = shap_values[0, :, 1]

else:
    values = shap_values[0]

importance = pd.DataFrame({
    "Feature": data.columns,
    "Impact": abs(values)
})

importance = importance.sort_values(
    by="Impact",
    ascending=False
)

print(importance)