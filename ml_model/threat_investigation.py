import pandas as pd


def threat_investigation():

    print("=" * 60)
    print("THREAT INVESTIGATION")
    print("=" * 60)

    # --------------------------------------------------
    # Load Risk Score Dataset
    # --------------------------------------------------

    data = pd.read_csv("../dataset/risk_scores.csv")

    print("\nRisk Score Dataset Loaded")
    print("Shape :", data.shape)

    # --------------------------------------------------
    # Filter High Risk Users
    # --------------------------------------------------

    high_risk = data[
        data["risk_level"].isin(["High", "Critical"])
    ]

    # --------------------------------------------------
    # Sort by Risk Score
    # --------------------------------------------------

    high_risk = high_risk.sort_values(
        by="risk_score",
        ascending=False
    )

    # --------------------------------------------------
    # Display Results
    # --------------------------------------------------

    print("\nHigh Risk Users")

    print(
        high_risk[
            [
                "user",
                "activity_date",
                "risk_score",
                "risk_level",
                "anomaly_score"
            ]
        ].head(20)
    )

    print("\nTotal High/Critical Cases :", len(high_risk))

    # --------------------------------------------------
    # Save Report
    # --------------------------------------------------

    high_risk.to_csv(
        "../dataset/high_risk_users.csv",
        index=False
    )

    print("\nThreat Investigation Report Saved Successfully")
    print("../dataset/high_risk_users.csv")


if __name__ == "__main__":
    threat_investigation()