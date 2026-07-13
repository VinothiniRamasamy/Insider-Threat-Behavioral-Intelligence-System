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

# 📊 Weekly Progress

## ✅ Week 1 – Machine Learning Development

- Collected and analyzed the CERT Insider Threat Dataset to understand employee behavioral activities.
- Preprocessed the raw datasets by cleaning missing values, formatting timestamps, and preparing structured data.
- Performed feature engineering to extract behavioral features from logon, web, device, file, and email activities.
- Trained a Random Forest Classification model to classify employee behavior as Normal User or Insider Threat.
- Evaluated the model performance and serialized the trained model using Joblib.
- Integrated SHAP (SHapley Additive Explanations) to generate feature importance and explain prediction results.

---

## ✅ Week 2 – Backend and Frontend Development

- Developed the backend using FastAPI and integrated the trained Random Forest model for real-time prediction.
- Created prediction APIs to return prediction results, confidence scores, and SHAP feature importance.
- Designed a professional employee login page using React.js with a clean and responsive user interface.
- Developed the prediction page to collect employee behavioral features and display prediction results.
- Integrated the React frontend with the FastAPI backend for seamless communication.
- Tested the complete workflow to ensure accurate predictions and proper frontend-backend integration.

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

## 🔐 Employee Login Page

![Login Page](screenshots/login.png)

## 📖 Employee Behavior Guide

![Behavior Guide](screenshots/behavior-guide.png)

## 📊 Prediction Dashboard

![Prediction Dashboard](screenshots/prediction-dashboard.png)
