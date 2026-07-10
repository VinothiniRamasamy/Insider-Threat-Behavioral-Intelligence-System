import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt


print("Loading Model and Dataset...")


# Load trained model
model = joblib.load("../dataset/insider_threat_model.pkl")


# Load processed feature dataset
data = pd.read_csv("../dataset/final_features.csv")


# Separate features
X = data.drop(["user", "label"], axis=1)


print("Creating SHAP Explainer...")


# Create SHAP Tree Explainer
explainer = shap.TreeExplainer(model)


# Calculate SHAP values
shap_values = explainer.shap_values(X)


print("SHAP Analysis Completed!")


print("Generating Feature Importance Plot...")


# Check SHAP output type

if isinstance(shap_values, list):

    # Binary classification old SHAP format
    shap_values_to_plot = shap_values[1]

elif len(shap_values.shape) == 3:

    # New SHAP format
    shap_values_to_plot = shap_values[:, :, 1]

else:

    # Regression / single output
    shap_values_to_plot = shap_values



# Generate Feature Importance Plot

shap.summary_plot(
    shap_values_to_plot,
    X,
    plot_type="bar",
    show=False
)


plt.title("Feature Importance - SHAP Analysis")


plt.tight_layout()


plt.savefig(
    "../dataset/shap_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()



print("Explainable AI Completed Successfully!")
print("SHAP plot saved as shap_feature_importance.png")