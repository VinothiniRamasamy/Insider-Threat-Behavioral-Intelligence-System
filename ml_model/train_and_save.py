import os
import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

BASE_DIR = r"C:\study\insider_threat_system"

# 1. Search for daily_user_features anywhere inside the project folder
target_file = None
for root, dirs, files in os.walk(BASE_DIR):
    for f in files:
        if "daily_user_features" in f:
            target_file = os.path.join(root, f)
            break
    if target_file:
        break

if not target_file:
    raise FileNotFoundError("Could not find 'daily_user_features' file anywhere in C:\\study\\insider_threat_system!")

print(f"✅ Found file at: {target_file}")

# 2. Read dataset
if target_file.endswith('.xlsx'):
    df = pd.read_excel(target_file)
else:
    df = pd.read_csv(target_file)

# 3. Apply Heuristic Labels
feature_columns = ['files_copied_to_usb', 'external_emails_sent', 'off_hours_logons', 
                   'distinct_pcs', 'sensitive_files_to_usb', 'cloud_job_visits', 'off_hours_usb']

feature_columns = [col for col in feature_columns if col in df.columns]
means = df[feature_columns].mean()

def assign_label(row):
    if row.get('files_copied_to_usb', 0) > means.get('files_copied_to_usb', 1) * 1.5 or row.get('external_emails_sent', 0) > means.get('external_emails_sent', 1) * 1.5:
        return 0  # Data Exfiltration
    elif row.get('off_hours_logons', 0) > means.get('off_hours_logons', 1) * 1.5 or row.get('distinct_pcs', 0) > means.get('distinct_pcs', 1) * 1.5:
        return 1  # IT Sabotage
    elif row.get('sensitive_files_to_usb', 0) > means.get('sensitive_files_to_usb', 1) * 1.5 or row.get('cloud_job_visits', 0) > means.get('cloud_job_visits', 1) * 1.5:
        return 2  # Intellectual Property Theft
    elif row.get('off_hours_usb', 0) > means.get('off_hours_usb', 1) * 1.5:
        return 4  # Unauthorized Access
    else:
        return 3  # Normal

df['Label'] = df.apply(assign_label, axis=1)

# 4. Clean Features: ONLY Keep Numeric Columns for Scaling & Training
drop_cols = ['user', 'day', 'date', 'Label']
X = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

# Select only numeric data types (float, int)
X = X.select_dtypes(include=[np.number])

# Fill any NaN values with 0
X = X.fillna(0)

y = df['Label']

# 5. Train Model & Scale Features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb.fit(X_train, y_train)

# 6. Save Artifacts inside ml_model folder
with open("gb.pkl", "wb") as f:
    pickle.dump(gb, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("feature_means.pkl", "wb") as f:
    pickle.dump(X_train.mean().to_dict(), f)

with open("feature_columns.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)

print("🎉 Model & Artifacts successfully saved as .pkl files inside ml_model folder!")