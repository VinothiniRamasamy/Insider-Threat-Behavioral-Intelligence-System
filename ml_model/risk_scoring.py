import pandas as pd


def risk_scoring():

    print("=" * 60)
    print("INSIDER RISK SCORING")
    print("=" * 60)

    # --------------------------------------------------
    # Load Anomaly Results
    # --------------------------------------------------

    data = pd.read_csv("../dataset/anomaly_results.csv")

    print("\nDataset Loaded Successfully")
    print("Shape :", data.shape)

    # --------------------------------------------------
    # Normalize Anomaly Score
    # --------------------------------------------------

    min_score = data["anomaly_score"].min()
    max_score = data["anomaly_score"].max()

    data["risk_score"] = (
        (data["anomaly_score"] - min_score)
        /
        (max_score - min_score)
    )

    # --------------------------------------------------
    # Risk Level
    # --------------------------------------------------

    def assign_risk(score):

        if score >= 0.80:
            return "Critical"

        elif score >= 0.60:
            return "High"

        elif score >= 0.40:
            return "Medium"

        else:
            return "Low"

    data["risk_level"] = data["risk_score"].apply(assign_risk)

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    print("\nRisk Level Summary")
    print(data["risk_level"].value_counts())

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    data.to_csv(
        "../dataset/risk_scores.csv",
        index=False
    )

    print("\nRisk Scores Saved Successfully")
    print("../dataset/risk_scores.csv")


if __name__ == "__main__":
    risk_scoring()