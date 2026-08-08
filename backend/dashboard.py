import streamlit as st
import pandas as pd
import os
import time

st.set_page_config(
    page_title="Insider Threat Monitoring Dashboard",
    layout="wide"
)

st.title("🛡 Insider Threat Behavioral Intelligence System")

st.write("### Live Prediction Dashboard")

log_file = "../dataset/prediction_logs.csv"

placeholder = st.empty()

while True:

    if os.path.exists(log_file):

        df = pd.read_csv(log_file)

        with placeholder.container():

            st.metric("Total Processed Logs", len(df))

            st.metric(
                "Anomalies",
                len(df[df["prediction"] == "Anomaly"])
            )

            st.metric(
                "Critical Users",
                len(df[df["risk_level"] == "Critical"])
            )

            st.write("### Latest Predictions")

            st.dataframe(
                df.tail(20),
                use_container_width=True
            )

    else:

        placeholder.warning(
            "Waiting for prediction logs..."
        )

    time.sleep(2)