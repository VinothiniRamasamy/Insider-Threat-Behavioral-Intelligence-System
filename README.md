# Insider-Threat-Behavioral-Intelligence-System

## Project Overview:

The Insider Threat Behavioral Intelligence System is an AI-powered web application that detects potential insider threats by analyzing employee behavioral activities. The system uses a Random Forest Classifier to classify employee behavior as Normal User or Insider Threat and provides Explainable AI (SHAP) insights to explain each prediction.

## Project Objectives:

Analyze employee behavioral activities.

Detect insider threats using Machine Learning.

Provide real-time predictions through a web application.

Explain prediction results using SHAP Explainable AI.

Assist organizations in identifying suspicious employee behavior.

## Current Progress

## Week 1 – Machine Learning Development

## Completed work:

Collected and preprocessed employee behavioral data.

Performed feature engineering.

Built the final training dataset.

Trained a Random Forest Classifier.

Evaluated the model and generated prediction results.

Saved the trained model for deployment.

## Week 2 – Application Development

## Completed work:

Developed the backend using FastAPI.

Built the frontend dashboard using React.js.

Connected the frontend with the backend API.

Integrated the trained ML model.

Implemented real-time prediction.

Added SHAP Explainable AI.

Displayed prediction results, confidence score, and feature importance on the dashboard.

## Input Features
The prediction model currently uses the following 9 behavioral features:

HTTP Count

After Hours

Unique PC

Unique URL

Logon Count

Device Count

File Count

Email Count

Unique Receivers

## Prediction Workflow:

User enters the 9 behavioral feature values.

The React frontend sends the data to the FastAPI backend.

The Random Forest model processes the input.

## The system predicts whether the employee is:

Normal User or 

Insider Threat

SHAP calculates the contribution of each feature.

The dashboard displays the prediction result.

## Sample Output:
## Prediction Result

Prediction: Normal User

Confidence Score: 52%

SHAP Feature Importance

The dashboard also displays the most influential features used by the model.

## Example:

Logon Count – 0.2410

Device Activity – 0.0977

Unique Files – 0.0839

File Count – 0.0784

Unique Receivers – 0.0783

These values help explain why the model classified the employee as a Normal User or Insider Threat.

Ongoing Development

## The following features are currently under development:

User Authentication (Login)

Input Validation

Prediction History

PostgreSQL Database Integration

Error Handling

Dashboard UI Enhancements

## Future Enhancements:

Risk Score Dashboard

User Role-Based Access Control

Prediction History Reports

Advanced Data Visualization

Model Performance Optimization

Cloud Deployment

Final Documentation and Testing
