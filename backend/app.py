from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import shap
import os


# -----------------------------------
# FastAPI App
# -----------------------------------

app = FastAPI(
    title="AI-Powered Insider Threat Detection API"
)


# -----------------------------------
# Enable CORS
# -----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------
# Load ML Model
# -----------------------------------

model_path = os.path.join("..", "ml_model", "model.pkl")

model = joblib.load(model_path)


# SHAP Explainer

explainer = shap.TreeExplainer(model)


# -----------------------------------
# Input Schema
# -----------------------------------

class UserInput(BaseModel):

    http_count: int
    after_hours: int
    unique_pc: int
    unique_url: int
    logon_count: int
    device_count: int
    device_activity: int
    file_count: int
    unique_files: int
    email_count: int
    total_attachment: int
    unique_receivers: int



# -----------------------------------
# Home Route
# -----------------------------------

@app.get("/")
def home():

    return {
        "message": "AI-Powered Insider Threat Detection API is Running"
    }



# -----------------------------------
# Prediction Route
# -----------------------------------

@app.post("/predict")
def predict(data: UserInput):


    features = pd.DataFrame([{

        "http_count": data.http_count,
        "after_hours": data.after_hours,
        "unique_pc": data.unique_pc,
        "unique_url": data.unique_url,
        "logon_count": data.logon_count,
        "device_count": data.device_count,
        "device_activity": data.device_activity,
        "file_count": data.file_count,
        "unique_files": data.unique_files,
        "email_count": data.email_count,
        "total_attachment": data.total_attachment,
        "unique_receivers": data.unique_receivers

    }])


    # Prediction

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]


    confidence = round(
        max(probability) * 100,
        2
    )


    if prediction == 1:

        result = "Insider"

    else:

        result = "Normal"



    # -------------------------------
    # SHAP Explanation
    # -------------------------------

    shap_values = explainer.shap_values(features)


    if isinstance(shap_values, list):

        values = shap_values[1][0]

    elif len(shap_values.shape) == 3:

        values = shap_values[0, :, 1]

    else:

        values = shap_values[0]


    values = values.flatten()


    explanation = {}


    for feature, value in zip(
        features.columns,
        values
    ):

        explanation[feature] = round(
            float(abs(value)),
            4
        )


    # Sort explanation

    explanation = dict(
        sorted(
            explanation.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )


    return {

        "prediction": result,

        "confidence": confidence,

        "explanation": explanation

    }