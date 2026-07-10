# Insider-Threat-Behavioral-Intelligence-System

🚀 Project Overview
This project is developed to detect insider threats by analyzing employee behavioral activity logs. Using a Machine Learning (Random Forest) model, it predicts whether an employee's behavior is Normal or an Insider Threat.

✅ What Has Been Done So Far

Backend: Built a REST API using FastAPI in Python.
Frontend: Built a dashboard using React.js that calls the backend API and displays the result.
ML Model: Trained a Random Forest Classifier model using employee behavioral data to make predictions.
Prediction Logic: When 9 behavioral details are provided as input, the data is sent to the model, which predicts whether the user is a Normal User or an Insider Threat and returns the output.

📊 9 Behavioral Features Given as Input 
HTTP Count - Website Requests
After Hours - Activity Outside Office Hours
Unique PC - Different Systems Used
Unique URL - Different Websites Visited
Logon Count - Login Frequency
Device Count - USB Devices Connected
File Count - Files Accessed
Email Count - Emails Sent
Unique Receivers - Different Email Receivers

⚙ How It Works

1.The user enters the above 9 details on the React frontend.
2.This data is sent to the FastAPI backend.
3.The Random Forest model in the backend processes the data and returns the prediction result (Normal / Insider Threat).
4.The result is displayed on the frontend dashboard.

📸 Sample Result

Prediction Output:
Prediction : Normal User
Confidence : 52%

Explainable AI (SHAP) Output – shows which features contributed most to the prediction:

logon_count         0.241
device_activity     0.0977
unique_files        0.0839
file_count          0.0784
unique_receivers    0.0783

So basically, after the user enters the 9 details, the dashboard shows:

1.Prediction – whether the user is a "Normal User" or "Insider Threat"
2.Confidence Score – how confident the model is about that prediction (in %)
3.Feature Importance – which behavioral features (like logon_count, device_activity, etc.) influenced the prediction the most, using SHAP values
