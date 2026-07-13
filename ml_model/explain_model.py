import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

print("Loading Model and Dataset...")

# -----------------------------------
# Load Model
# -----------------------------------

model = joblib.load("../dataset/insider_threat_model.pkl")

# -----------------------------------
# Load Dataset
# -----------------------------------

data = pd.read_csv("../dataset/final_features.csv")

# -----------------------------------
# Features Only
# -----------------------------------

X = data.drop(["user", "label"], axis=1)

print("Creating SHAP Explainer...")

# -----------------------------------
# SHAP Explainer
# -----------------------------------

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

print("SHAP Analysis Completed!")

print("Generating Feature Importance Plot...")

# -----------------------------------
# Handle Different SHAP Versions
# -----------------------------------

if isinstance(shap_values, list):

    # Older SHAP versions
    shap_values_to_plot = shap_values[1]

elif hasattr(shap_values, "values"):

    # New SHAP Explanation Object
    shap_values_to_plot = shap_values.values

    if len(shap_values_to_plot.shape) == 3:
        shap_values_to_plot = shap_values_to_plot[:, :, 1]

elif len(shap_values.shape) == 3:

    # New ndarray format
    shap_values_to_plot = shap_values[:, :, 1]

else:

    shap_values_to_plot = shap_values

# -----------------------------------
# Feature Importance Plot
# -----------------------------------

plt.figure(figsize=(10,6))

shap.summary_plot(
    shap_values_to_plot,
    X,
    plot_type="bar",
    show=False
)

plt.title("Feature Importance using SHAP")

plt.tight_layout()

plt.savefig(
    "../dataset/shap_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nExplainable AI Completed Successfully!")
print("SHAP plot saved as ../dataset/shap_feature_importance.png")