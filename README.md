# 🛡️ Insider Threat Behavioral Intelligence System

An AI-powered web application that detects potential insider threats by analyzing employee behavioral activities using Machine Learning and Explainable AI (SHAP). The system classifies employee behavior as **Normal User** or **Insider Threat** and provides transparent predictions with feature importance.

---

# 📌 Project Overview

The **Insider Threat Behavioral Intelligence System** is designed to help organizations identify suspicious employee activities before they lead to security incidents. It analyzes behavioral data such as login activity, web browsing, file access, email communication, and device usage to predict insider threats.

The application combines a **Random Forest Classifier**, **FastAPI**, **React.js**, and **SHAP Explainable AI** to provide accurate, real-time, and interpretable predictions.

---

# 🎯 Objectives

- Detect potential insider threats using Machine Learning.
- Analyze employee behavioral activities.
- Provide real-time predictions through a web application.
- Explain every prediction using SHAP Explainable AI.
- Improve organizational security through behavioral analytics.

---

# ✨ Features

- 🔐 Employee Login System
- 📊 Employee Behavior Monitoring
- 🤖 Machine Learning-Based Threat Detection
- ⚡ Real-Time Predictions
- 📈 Confidence Score Display
- 🧠 Explainable AI using SHAP
- 📉 Feature Importance Visualization
- 🌐 REST API using FastAPI
- 💻 Interactive React Dashboard

---

# 🛠️ Tech Stack

## Frontend
- React.js
- HTML5
- CSS3
- JavaScript
- Axios

## Backend
- FastAPI
- Python
- Uvicorn

## Machine Learning
- Scikit-learn
- Random Forest Classifier
- Pandas
- NumPy
- Joblib

## Explainable AI
- SHAP (SHapley Additive Explanations)

---

# 📂 Dataset

This project uses the **CERT Insider Threat Dataset**, which contains simulated employee activity logs.

The dataset includes:

- HTTP Activity
- Logon Activity
- Device Usage
- File Access
- Email Communication
- Insider User Labels

These logs are processed and transformed into behavioral features for machine learning.

---

# 📊 Behavioral Features

| Feature | Description |
|----------|-------------|
| http_count | Total number of websites visited |
| unique_url | Number of different websites accessed |
| logon_count | Total login and logout activities |
| unique_pc | Number of different computers used |
| after_hours | Activity outside office hours |
| device_count | Number of USB devices connected |
| device_activity | Total USB activities |
| file_count | Total files accessed |
| unique_files | Number of different files accessed |
| email_count | Total emails handled |
| total_attachment | Total email attachments |
| unique_receivers | Number of different email recipients |

---

# ⚙️ Machine Learning Workflow

```
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
Random Forest Classifier
        │
        ▼
Prediction
        │
        ▼
SHAP Explainable AI
        │
        ▼
Prediction Dashboard
```

---

# 🔄 Application Workflow

```
Employee Behavioral Data
          │
          ▼
React Frontend
          │
          ▼
FastAPI Backend
          │
          ▼
Machine Learning Model
          │
          ▼
Prediction Engine
          │
          ▼
SHAP Explainable AI
          │
          ▼
Prediction Dashboard
```

---

# 🎯 Prediction Output

The system predicts one of the following:

### ✅ Normal User

Employee behavior appears normal without suspicious activities.

### 🚨 Insider Threat

Employee behavior indicates patterns that may represent a potential insider threat.

Each prediction includes:

- Prediction Label
- Confidence Score
- SHAP Feature Importance
- Most Influential Behavioral Features

---

# 📈 Sample Prediction

```
Prediction        : Insider Threat
Confidence Score  : 94.67%

Top Important Features

Device Count       : 0.1164
Logon Count        : 0.1062
Device Activity    : 0.0928
Unique Files       : 0.0632
Unique PC          : 0.0500
```

---

# 🧠 Explainable AI

This project integrates **SHAP (SHapley Additive Explanations)** to make model predictions transparent.

SHAP helps by:

- Explaining every prediction.
- Showing the contribution of each feature.
- Identifying the most influential behavioral activities.
- Increasing trust in the machine learning model.

---

# 📁 Project Structure

```
Insider-Threat-Behavioral-Intelligence-System
│
├── backend
│
├── frontend
│
├── ml_model
│
├── screenshots
│
├── README.md
│
└── requirements.txt
```

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/VinothiniRamasamy/Insider-Threat-Behavioral-Intelligence-System.git
```

---

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm start
```

---


# 🎯 Future Enhancements

- Deep Learning-Based Detection
- Real-Time Activity Monitoring
- Live Log Streaming
- Email Alert System
- Admin Dashboard
- User Role Management
- Cloud Deployment (AWS)
- Docker Containerization

---

# 👩‍💻 Author

**Vinothini R**

Bachelor of Engineering (Artificial Intelligence and Data Science)

GitHub:
https://github.com/VinothiniRamasamy

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
