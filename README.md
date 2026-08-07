# 🛡️ Insider Threat Behavioral Intelligence System

An AI-powered Insider Threat Behavioral Intelligence System that detects suspicious employee activities by analyzing behavioral deviations from historical patterns. The system uses Machine Learning to identify insider threats, assign dynamic risk scores, and provide real-time monitoring through a FastAPI backend and React dashboard.

---

# 📖 Overview

Insider threats remain one of the most difficult cybersecurity challenges because malicious or negligent employees already possess authorized access to organizational resources.

This project analyzes employee behavioral logs collected from enterprise systems and compares current activities with historical behavioral baselines. Machine Learning models are then used to identify abnormal behavior, estimate risk levels, and assist security analysts in investigating potential insider threats.

The application supports real-time prediction streaming, explainable risk analysis, and interactive visualization through a web dashboard.

---

# 🎯 Objectives

- Detect suspicious employee behavior using Machine Learning.
- Build behavioral baselines for every employee.
- Identify deviations from normal user activities.
- Calculate dynamic insider risk scores.
- Stream predictions in real time.
- Provide an easy-to-use dashboard for security analysts.

---

# 🚀 Key Features

- Employee Behavioral Profiling
- Feature Engineering from CERT logs
- Behavior Baseline Generation
- Behavior Deviation Analysis
- Gradient Boosting Machine Learning Model
- Explainable Predictions
- Dynamic Risk Scoring
- FastAPI REST API
- Real-Time Prediction Streaming
- React Dashboard
- Docker Support

---

# 🤖 Machine Learning Pipeline

```text
CERT Insider Threat Dataset
            │
            ▼
      Data Preprocessing
            │
            ▼
     Feature Engineering
            │
            ▼
  Behavioral Baseline Creation
            │
            ▼
 Behavior Deviation Calculation
            │
            ▼
      Feature Standardization
            │
            ▼
 Gradient Boosting Classifier
            │
            ▼
     Insider Threat Prediction
            │
            ▼
      Risk Score Calculation
            │
            ▼
    Prediction Explanation
            │
            ▼
      FastAPI REST Backend
            │
            ▼
   React Real-Time Dashboard
```

---

# 📊 Machine Learning Workflow

## 1. Data Preprocessing

The CERT Insider Threat dataset contains multiple log sources including:

- Logon Logs
- Device Logs
- Email Logs
- HTTP Logs
- File Access Logs

During preprocessing:

- Missing values were handled
- Duplicate records were removed
- Timestamp fields were standardized
- Clean datasets were generated

Output Files:

- logon_clean.csv
- device_clean.csv
- email_clean.csv
- file_clean.csv
- http_clean.csv

---

## 2. Feature Engineering

Behavioral features were extracted for every employee.

Important features include:

- Logon Count
- Off Hours Logons
- Distinct PCs Used
- USB Connections
- Off Hours USB Usage
- Files Copied to USB
- Sensitive Files Copied
- Total Emails Sent
- External Emails
- Email Attachments
- Email Size
- HTTP Requests
- Cloud Job Visits

Generated Dataset:

- daily_user_features.csv

---

## 3. Behavioral Baseline Generation

Historical user activities were aggregated to calculate the normal behavioral profile for every employee.

Generated File:

- behavior_baseline.csv

---

## 4. Behavior Deviation Calculation

Current user activity is compared against the behavioral baseline to compute deviations.

Generated File:

- behavior_deviation.csv

---

## 5. Feature Scaling

Numerical features are standardized using StandardScaler before prediction.

Saved Model:

- scaler.pkl

---

## 6. Machine Learning Model

The project uses a **Gradient Boosting Classifier** to classify employee behavior.

Model artifacts:

- gb.pkl
- feature_columns.pkl
- feature_means.pkl

---

## 7. Risk Score Calculation

Predicted behaviors are converted into risk scores using weighted behavioral features.

Risk Levels:

| Score | Risk |
|-------|------|
| 0 – 9 | Low Risk |
| 10 – 19 | Medium Risk |
| 20+ | High Risk |

Generated Outputs:

- risk_scores.csv
- high_risk_users.csv

---

## 8. Explainable Predictions

Prediction explanations identify the important behavioral features influencing each prediction.

Generated File:

- explained_predictions.csv

---

## 9. Real-Time Threat Monitoring

The FastAPI backend streams live predictions to the React dashboard.

Displayed Information:

- Employee ID
- Prediction
- Risk Score
- Risk Category
- Timestamp

---

# 🛠️ Technology Stack

## Programming

- Python
- JavaScript

## Machine Learning

- Scikit-Learn
- Gradient Boosting Classifier

## Data Processing

- Pandas
- NumPy

## Backend

- FastAPI
- Uvicorn

## Frontend

- React.js

## Deployment

- Docker
- Docker Compose

---

# 📂 Project Structure

```
Insider_Threat_Behavioral_Intelligence_System

│
├── backend
│   ├── app.py
│   ├── dashboard.py
│   ├── live_feature_engine.py
│   ├── sample_data.py
│   ├── stream_processor.py
│   ├── user_activity.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── dataset
│   ├── logon_clean.csv
│   ├── device_clean.csv
│   ├── email_clean.csv
│   ├── file_clean.csv
│   ├── http_clean.csv
│   ├── daily_user_features.csv
│   ├── behavior_baseline.csv
│   ├── behavior_deviation.csv
│   ├── anomaly_results.csv
│   ├── risk_scores.csv
│   ├── explained_predictions.csv
│   ├── high_risk_users.csv
│   └── isolation_forest_model.pkl
│
├── ml_model
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── behavior_baseline.py
│   ├── behavior_deviation.py
│   ├── anomaly_detection.py
│   ├── risk_scoring.py
│   ├── explain_prediction.py
│   ├── threat_investigation.py
│   ├── train_and_save.py
│   ├── gb.pkl
│   ├── scaler.pkl
│   ├── feature_columns.pkl
│   └── feature_means.pkl
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── README.md
│
└── docker-compose.yml
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Insider-Threat-Behavioral-Intelligence-System.git

cd Insider-Threat-Behavioral-Intelligence-System
```

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm start
```

Frontend:

```
http://localhost:3000
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API Status |
| POST | /token | User Authentication |
| GET | /stream | Real-Time Prediction Stream |

---

# 📊 Dashboard Features

The React dashboard displays:

- Total Processed Logs
- Detected Anomalies
- Critical Users
- Risk Scores
- Live Prediction Table
- Real-Time Monitoring

---

# 🐳 Docker Deployment

```bash
docker-compose up --build
```

---

# 🔮 Future Enhancements

- JWT Authentication
- Role-Based Access Control
- Email Alert Notifications
- SIEM Integration
- SHAP-Based Explainable AI
- Cloud Deployment (AWS/Azure)
- Kafka-Based Real-Time Streaming
- Advanced Threat Investigation Module

---

# 📚 Dataset

**CERT Insider Threat Dataset (CMU CERT)**

The dataset contains enterprise activity logs including:

- Logon Activities
- Device Activities
- File Operations
- Email Communications
- HTTP Browsing Records

---

# 👩‍💻 Developer

**Vinothini R**

B.Tech – Artificial Intelligence and Data Science


---

# 📌 Project Highlights

- AI-Based Insider Threat Detection
- Behavioral Analytics
- Machine Learning Pipeline
- Explainable Predictions
- Dynamic Risk Scoring
- FastAPI Backend
- React Frontend
- Real-Time Monitoring Dashboard
- Dockerized Deployment
