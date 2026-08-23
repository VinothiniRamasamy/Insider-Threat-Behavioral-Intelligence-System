# 🛡️ Insider Threat Behavioral Intelligence System

An AI-powered Insider Threat Behavioral Intelligence System that detects suspicious employee activities by analyzing behavioral deviations from historical patterns. The system uses Machine Learning to identify insider threats, assign dynamic risk scores, and provide real-time monitoring through a FastAPI backend and React dashboard.

---

## 🚀 Project Overview

The platform provides an end-to-end workflow for insider threat detection:

**Activity Logs → Feature Engineering → Behavioral Baselines → ML Detection → UEBA Risk Scoring → Alerts → Investigation → Reports**

The system combines:

- 🤖 Machine Learning-based threat classification
- 📊 User behavioral profiling
- ⚖️ Dynamic risk scoring
- 🔍 SHAP-based explainable AI
- 🚨 Real-time threat alerts
- 📡 Server-Sent Events (SSE) activity streaming
- 📄 PDF case report generation
- 📊 Excel log export
- 🖥️ Interactive React security console

---

## ✨ Key Features

### 🔐 1. User Authentication & RBAC

- Analyst login authentication
- Role-based portal access
- Secure analyst session management

### 👤 2. Employee Profiles

- Employee identity tracking
- User-specific behavioral information
- Historical activity baseline management

### 📡 3. Real-Time Activity Monitoring

- Monitors user activity events
- Server-Sent Events (SSE) based streaming
- Near real-time activity visualization
- Activity refresh approximately every 1.5 seconds

### 📊 4. Behavioral Profiling

- Creates per-user daily behavioral profiles
- Calculates historical activity averages
- Maintains behavioral baselines using:


daily_user_features.csv


### 🚨 5. Anomaly Detection

- Compares current activity against historical behavioral patterns
- Detects abnormal deviations
- Identifies potentially suspicious user behavior

### ⚖️ 6. Dynamic Risk Scoring

Generates a composite risk score between:

**0 – 100**

The score is calculated using weighted behavioral risk indicators.

### 🔍 7. Threat Investigation

Security analysts can investigate suspicious employees using:

- Behavioral deviations
- Risk scores
- SHAP feature contributions
- Activity evidence
- User-specific investigation reports

### 🧠 8. UEBA Intelligence

The UEBA engine establishes behavioral baselines and identifies deviations from normal user activity.

### 🚨 9. Incident Alerts Queue

Displays high-risk users and suspicious activities with severity classifications.

### 📈 10. Executive Dashboard

Provides high-level enterprise security statistics such as:

- Threat counts
- Risk distribution
- User activity statistics
- System monitoring information

### 🔔 11. Notifications & Severity Flags

Automatically categorizes detected risks into:

- 🔴 Critical
- 🟠 High
- 🟡 Medium
- 🔵 Low

### 📄 12. Reports & Exports

Supports generation of:

- PDF investigation case files
- Excel activity/risk logs

### 🔗 13. End-to-End Integration

Integrates:

**React Frontend + FastAPI Backend + ML Model + UEBA Risk Engine**

into a single security monitoring platform.

---

## 🏗️ System Architecture

---

## 🔬 ML & Risk Detection Pipeline

The system processes raw CERT activity logs and converts them into daily user behavioral features.

---

## ⚙️ How Detection Works

### Step 1 — Data Ingestion

The platform uses activity logs from the **CERT Insider Threat Benchmark Dataset r4.2**.

The major activity sources include:

- Logon activity
- Device activity
- File activity
- Email activity
- HTTP activity

### Step 2 — Feature Engineering

Raw event logs are aggregated into daily user-level behavioral features.

The generated dataset is:


dataset/daily_user_features.csv


### Step 3 — Behavioral Baselines

Historical user activity is used to establish normal behavioral patterns.

The system maintains baseline feature information using:


ml_model/feature_means.pkl


### Step 4 — Machine Learning Detection

The processed features are passed to a trained:

**Gradient Boosting Classifier**

The trained model is stored as:


ml_model/gb.pkl


Feature scaling is handled using:


ml_model/scaler.pkl


### Step 5 — UEBA Risk Calculation

The system combines machine learning detection with weighted behavioral risk indicators.

### Step 6 — Composite Risk Score

A final score between **0 and 100** is generated.

### Step 7 — Alert Generation

High-risk activity is added to the incident alert queue for further investigation.

### Step 8 — Investigation

Security analysts can inspect:

- User behavior
- Risk score
- Behavioral deviations
- Important features
- SHAP explanations
- Activity timeline

### Step 9 — Reporting

Investigation results can be exported as:

- PDF case files
- Excel reports

---

## ⚖️ Risk Scoring & Severity Pipeline

The UEBA engine calculates the composite risk score using weighted behavioral indicators.

| **Risk ComponentWeight** |    |
| ------------------------ | -- |
| Files Copied to USB      | 3× |
| Off-Hours USB Activity   | 3× |
| External Email Volume    | 3× |
| Off-Hours Logons         | 2× |
| Cloud Job Visits         | 2× |

### Severity Levels

| **ScoreSeverity** |             |
| ----------------- | ----------- |
| ≥ 80              | 🔴 Critical |
| ≥ 60              | 🟠 High     |
| ≥ 40              | 🟡 Medium   |
| < 40              | 🔵 Low      |

---

## 🔍 Explainable AI with SHAP

The platform uses **SHAP (SHapley Additive exPlanations)** to provide explainability for ML predictions.

SHAP helps the analyst understand:

- Which behavioral features contributed to the prediction
- Which activities increased risk
- Which activities reduced risk
- Why a particular user was flagged

This improves the interpretability of the insider threat detection process.

---

## 🔄 Forensic Case Investigation Workflow

When an analyst investigates a suspicious employee:

Example case report:


Investigation_Report_AAE0190.pdf


---

## 🖥️ Security Console

The React frontend provides six primary pages:

1. 📊 Dashboard
2. 📡 Live Monitoring
3. 🧠 Behavioral Profiling
4. 🚨 Threat Alerts
5. 🔍 Investigation
6. 📄 Reports

The console uses a responsive dark cybersecurity-themed interface.

---

## 🧩 Module Implementation Status

| **#ModuleStatusKey Functionality** |                       |   |                                              |
| ---------------------------------- | --------------------- | - | -------------------------------------------- |
| 1                                  | User Auth & RBAC      | ✅ | Analyst authentication and role-based access |
| 2                                  | Employee Profiles     | ✅ | Identity tracking and baseline profiles      |
| 3                                  | Activity Monitor      | ✅ | Real-time SSE activity streaming             |
| 4                                  | Behavioral Profiling  | ✅ | Per-user daily behavioral baselines          |
| 5                                  | Anomaly Detection     | ✅ | Historical deviation detection               |
| 6                                  | Risk Scoring          | ✅ | Dynamic 0–100 risk score                     |
| 7                                  | Threat Investigation  | ✅ | SHAP analysis and evidence timeline          |
| 8                                  | UEBA Intelligence     | ✅ | Behavioral baseline and deviation tracking   |
| 9                                  | Incident Alerts Queue | ✅ | High-risk threat monitoring                  |
| 10                                 | Executive Dashboard   | ✅ | Enterprise-level threat statistics           |
| 11                                 | Notifications & Flags | ✅ | Automatic severity classification            |
| 12                                 | Reports & Exports     | ✅ | PDF and Excel generation                     |
| 13                                 | Integration & Demo    | ✅ | Full-stack end-to-end integration            |

---

## 🧰 Technology Stack

| **LayerTechnologies** |                                    |
| --------------------- | ---------------------------------- |
| Backend API           | Python 3.12, FastAPI, Uvicorn      |
| API Communication     | REST API, Server-Sent Events (SSE) |
| Authentication        | OAuth2, JWT                        |
| Data Validation       | Pydantic                           |
| Machine Learning      | Scikit-learn                       |
| ML Algorithm          | Gradient Boosting Classifier       |
| Feature Scaling       | MinMaxScaler                       |
| Data Processing       | Pandas, NumPy                      |
| Explainable AI        | SHAP                               |
| Frontend              | React.js 18                        |
| UI                    | HTML5, CSS3, Responsive Dark Theme |
| PDF Generation        | ReportLab                          |
| Excel Generation      | OpenPyXL                           |
| Dataset               | CERT Insider Threat Dataset r4.2   |

---

## 📁 Repository Structure

.
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── ml_model/
│   ├── gb.pkl
│   ├── scaler.pkl
│   ├── feature_means.pkl
│   └── feature_columns.pkl
│
├── dataset/
│   └── daily_user_features.csv
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Sidebar.js
│   │   │   └── LoginPage.js
│   │   │
│   │   ├── pages/
│   │   │   ├── DashboardPage.js
│   │   │   ├── LiveMonitoringPage.js
│   │   │   ├── BehavioralProfilingPage.js
│   │   │   ├── ThreatAlertsPage.js
│   │   │   ├── InvestigationPage.js
│   │   │   └── ReportsPage.js
│   │   │
│   │   └── App.js
│   │
│   └── package.json
│
└── README.md

---

## ⚡ Installation & Setup

### 1. Clone the Repository


git clone <YOUR_REPOSITORY_URL>
cd Insider-Threat-Behavioral-Intelligence-System


### 2. Start the FastAPI Backend

Open a new terminal and navigate to the backend:


cd backend


Install dependencies:


pip install -r requirements.txt


Start the FastAPI server:


uvicorn app:app --reload --port 8000


Backend API:


http://localhost:8000


Interactive API Documentation:


http://localhost:8000/docs


### 3. Launch React Security Console

Open another terminal:


cd frontend


Install dependencies:


npm install


Start the React development server:


npm start


Security Portal Console:


http://localhost:3000


---

## 🔗 Application URLs

| **ServiceURL**         |                              |
| ---------------------- | ---------------------------- |
| React Security Console | `http://localhost:3000`      |
| FastAPI Backend        | `http://localhost:8000`      |
| FastAPI Swagger Docs   | `http://localhost:8000/docs` |
| SSE Activity Stream    | `/stream`                    |
| PDF Export             | `/api/v1/export/pdf`         |
| Excel Export           | `/api/v1/export/excel`       |

---

## 🔌 API Endpoints

### Activity Stream


GET /stream


Provides real-time activity updates using Server-Sent Events.

### PDF Investigation Report


GET /api/v1/export/pdf


Generates a user-specific investigation case file.

### Excel Export


GET /api/v1/export/excel


Exports relevant activity and risk information in Excel format.

---

## 📊 Data Flow


CERT r4.2 Dataset
↓
Data Ingestion
↓
Feature Engineering
↓
Daily User Features
↓
Historical Behavioral Baselines
↓
Gradient Boosting Classifier
↓
UEBA Risk Engine
↓
Composite Risk Score
↓
Severity Classification
↓
Incident Alert Queue
↓
Threat Investigation
↓
PDF / Excel Reports


---

## 🎯 Project Objectives

The main objectives of this project are:

- To monitor employee behavioral activities.
- To establish normal behavioral profiles for users.
- To identify unusual activity patterns.
- To detect potential insider threats using machine learning.
- To calculate dynamic behavioral risk scores.
- To provide explainable ML predictions using SHAP.
- To generate real-time security alerts.
- To assist analysts during forensic investigations.
- To generate structured investigation reports.
- To provide an integrated enterprise security monitoring console.

---

## 🌟 Advantages

- **AI-powered threat detection**
- **Behavior-based monitoring**
- **Dynamic risk scoring**
- **Explainable AI**
- **Real-time monitoring**
- **Automated alert generation**
- **Forensic investigation support**
- **PDF and Excel reporting**
- **Full-stack architecture**
- **Enterprise-style security dashboard**

---

## 🔮 Future Enhancements

Potential future improvements include:

- Advanced deep learning-based behavioral detection
- Real-time database integration
- Email/SMS notification integration
- More advanced anomaly detection algorithms
- Automated incident response workflows
- Cloud deployment using AWS
- Docker containerization
- Multi-organization support
- Advanced threat correlation
- Historical risk trend visualization

---

## 📚 Dataset

This project uses the:

**CERT Insider Threat Dataset r4.2**

The dataset contains simulated employee activity logs covering multiple activity categories, including:

- Logon
- Device
- File
- Email
- HTTP/Web activity

The dataset is used for behavioral analysis, feature engineering, machine learning, and UEBA-based risk assessment.

---

## 🏁 Project Status

**Status: ✅ Fully Implemented**

The current version includes the complete workflow:


Authentication
↓
Employee Monitoring
↓
Behavioral Profiling
↓
Anomaly Detection
↓
ML Threat Detection
↓
UEBA Risk Scoring
↓
Incident Alerts
↓
Threat Investigation
↓
Reports & Exports


---

## 👩‍💻 Project Information

### Enterprise Insider Threat UEBA Intelligence Platform

**Technologies:** Python · FastAPI · React.js · Scikit-learn · SHAP · Pandas · NumPy · ReportLab · OpenPyXL

**Dataset:** CERT Insider Threat Dataset r4.2

---

## ⭐ If You Find This Project Useful

Give the repository a ⭐ and feel free to explore the implementation.

---

### Author

**Vinothini R**

B.Tech – Artificial Intelligence and Data Science
