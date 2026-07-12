# Insider-Threat-Behavioral-Intelligence-System

## 📌 Project Overview

The Insider Threat Behavioral Intelligence System is an AI-powered web application designed to detect potential insider threats by analyzing employee behavioral activities. The system leverages Machine Learning (Random Forest Classifier) to classify employee behavior as either Normal User or Insider Threat. Additionally, it uses SHAP (SHapley Additive Explanations) to explain the reasoning behind every prediction, making the model transparent and interpretable.

## 🎯 Project Objectives

Analyze employee behavioral activities.

Detect potential insider threats using Machine Learning.

Provide real-time predictions through a web application.

Explain prediction results using SHAP Explainable AI.

Help organizations identify suspicious employee behavior at an early stage.

## 📂 Dataset

This project uses the CERT Insider Threat Dataset, which contains simulated employee activity logs.

The dataset includes:

HTTP Activity

Logon Activity

Device Usage

File Access

Email Communication

Insider User Labels

These logs are processed to generate behavioral features for machine learning.

## ⚙️ Machine Learning Workflow
Raw CERT Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Training Dataset
        │
        ▼
Random Forest Model
        │
        ▼
Prediction
        │
        ▼
SHAP Explainable AI
        │
        ▼
React Dashboard

## 📊 Current Progress
## ✅ Week 1 – Machine Learning Development

Completed:

Data Collection. 

Data Preprocessing

Feature Engineering

Model Training

Model Evaluation

Random Forest Classification

Model Serialization

SHAP Analysis

## ✅ Week 2 – Application Development

Completed:

FastAPI Backend

React Frontend

API Integration

Real-time Prediction

SHAP Integration

Confidence Score Display

Feature Importance Display

## 📋 Behavioral Features

Feature	Description

http_count --	Total number of websites visited by the employee.

unique_url --	Number of different websites accessed.

logon_count --	Total login and logout activities.

unique_pc --	Number of different computers used.

after_hours	-- Activities performed outside office hours.

device_count --	Number of USB or external devices connected.

device_activity --	Total USB-related activities.

file_count --	Total files accessed or modified.

unique_files --	Number of different files accessed.

email_count --	Total emails sent or received.

total_attachment --	Total email attachments handled.

unique_receivers --	Number of different email recipients.

## 🔄 Prediction Workflow
User Inputs Behavioral Features
               │
               ▼
React Frontend
               │
               ▼
FastAPI Backend
               │
               ▼
Random Forest Model
               │
               ▼
Prediction
(Normal / Insider)
               │
               ▼
Confidence Score
               │
               ▼
SHAP Explainable AI
               │
               ▼
Feature Importance Display

## 🎯 Prediction Output

The model predicts one of the following:

✅ Normal User

Employee behavior appears normal and does not indicate suspicious insider activity.

🚨 Insider Threat

Employee behavior shows patterns that may indicate a potential insider threat.

Each prediction includes:

Prediction Label

Confidence Score

SHAP Feature Importance

## 📈 Sample Output
Example Prediction

Prediction : Insider Threat

Confidence : 94.67%

Top Important Features

Feature	SHAP Value

Device Count	0.1164 ,
Logon Count	0.1062 ,
Device Activity	0.0928 ,
Unique Files	0.0632 ,
Unique PC	0.0500

These values explain why the model classified the employee as an Insider Threat.

The project integrates SHAP (SHapley Additive Explanations) to improve model transparency.

SHAP helps by:

1.Explaining every prediction.
2.Showing the contribution of each feature.
3.Identifying the most influential behavioral activities.
4.Increasing trust in the machine learning model.

## 📌 Project Architecture
React Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
Random Forest Model
      │
      ▼
Prediction Engine
      │
      ▼
SHAP Explainable AI
      │
      ▼
Prediction Dashboard
