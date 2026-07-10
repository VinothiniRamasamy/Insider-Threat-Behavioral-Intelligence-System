import pandas as pd
import joblib
import shap


print("Loading Model...")


# Load trained model
model = joblib.load("model.pkl")


# Create SHAP Explainer
explainer = shap.TreeExplainer(model)


print("Enter User Activity Details")


http_count = int(input("Enter HTTP Count: "))
after_hours = int(input("After Hours Activity (1/0): "))
unique_pc = int(input("Enter Unique PC Count: "))
unique_url = int(input("Enter Unique URL Count: "))
logon_count = int(input("Enter Logon Count: "))
device_count = int(input("Enter Device Count: "))
device_activity = int(input("Enter Device Activity Count: "))
file_count = int(input("Enter File Count: "))
unique_files = int(input("Enter Unique Files Count: "))
email_count = int(input("Enter Email Count: "))
total_attachment = int(input("Enter Total Attachment Count: "))
unique_receivers = int(input("Enter Unique Receivers Count: "))


# Create input dataframe
# Same features used in train_model.py

data = pd.DataFrame([{

    "http_count": http_count,
    "after_hours": after_hours,
    "unique_pc": unique_pc,
    "unique_url": unique_url,
    "logon_count": logon_count,
    "device_count": device_count,
    "device_activity": device_activity,
    "file_count": file_count,
    "unique_files": unique_files,
    "email_count": email_count,
    "total_attachment": total_attachment,
    "unique_receivers": unique_receivers

}])


# Prediction

prediction = model.predict(data)


if prediction[0] == 1:

    print("\nRisk Level : HIGH")
    print("Prediction : Insider Threat")

else:

    print("\nRisk Level : LOW")
    print("Prediction : Normal User")



# =========================
# SHAP Explanation
# =========================

print("\nImportant Factors:")


shap_values = explainer.shap_values(data)


# Handle different SHAP versions

if isinstance(shap_values, list):

    values = shap_values[1][0]


elif len(shap_values.shape) == 3:

    values = shap_values[0, :, 1]


else:

    values = shap_values[0]


values = values.flatten()


# Create importance dataframe

importance = pd.DataFrame({

    "Feature": data.columns,
    "Impact": abs(values)

})


print(
    importance.sort_values(
        by="Impact",
        ascending=False
    )
)