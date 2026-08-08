import pandas as pd


def explain_prediction():

    print("=" * 60)
    print("PREDICTION EXPLANATION")
    print("=" * 60)

    # --------------------------------------------------
    # Load High Risk Dataset
    # --------------------------------------------------

    data = pd.read_csv("../dataset/high_risk_users.csv")

    print("\nHigh Risk Dataset Loaded")
    print("Shape :", data.shape)

    # --------------------------------------------------
    # Deviation Columns
    # --------------------------------------------------

    deviation_columns = [
        "http_count_deviation",
        "unique_url_deviation",
        "logon_count_deviation",
        "unique_pc_deviation",
        "device_count_deviation",
        "file_count_deviation",
        "unique_files_deviation",
        "email_count_deviation",
        "unique_receivers_deviation",
        "total_attachment_deviation"
    ]

    # --------------------------------------------------
    # Generate Explanation
    # --------------------------------------------------

    def explain(row):

        values = {}

        for col in deviation_columns:
            values[col] = abs(row[col])

        top3 = sorted(
            values.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        explanation = ", ".join(
            [
                item[0].replace("_deviation", "")
                for item in top3
            ]
        )

        return explanation

    data["reason"] = data.apply(
        explain,
        axis=1
    )

    # --------------------------------------------------
    # Display Sample
    # --------------------------------------------------

    print("\nPrediction Explanation")

    print(
        data[
            [
                "user",
                "risk_level",
                "risk_score",
                "reason"
            ]
        ].head(20)
    )

    # --------------------------------------------------
    # Save Results
    # --------------------------------------------------

    data.to_csv(
        "../dataset/explained_predictions.csv",
        index=False
    )

    print("\nExplanation Saved Successfully")
    print("../dataset/explained_predictions.csv")


if __name__ == "__main__":
    explain_prediction()