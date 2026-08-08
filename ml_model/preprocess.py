import pandas as pd

def preprocess():

    print("=" * 60)
    print("DATA PREPROCESSING")
    print("=" * 60)

    # --------------------------------------------------
    # Load Datasets
    # --------------------------------------------------

    http = pd.read_csv("../dataset/http.csv", nrows=100000)
    logon = pd.read_csv("../dataset/logon.csv", nrows=100000)
    device = pd.read_csv("../dataset/device.csv", nrows=100000)
    file = pd.read_csv("../dataset/file.csv", nrows=100000)
    email = pd.read_csv("../dataset/email.csv", nrows=100000)
    insiders = pd.read_csv("../dataset/insiders.csv")

    print("\nDatasets Loaded Successfully")
    print("HTTP    :", http.shape)
    print("LOGON   :", logon.shape)
    print("DEVICE  :", device.shape)
    print("FILE    :", file.shape)
    print("EMAIL   :", email.shape)
    print("INSIDERS:", insiders.shape)

    # --------------------------------------------------
    # Data Cleaning
    # --------------------------------------------------

    datasets = {
        "http": http,
        "logon": logon,
        "device": device,
        "file": file,
        "email": email
    }

    for name, df in datasets.items():

        # Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # Remove rows with missing values
        df.dropna(inplace=True)

        # Convert date column
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])

    print("\nData Cleaning Completed")

    # --------------------------------------------------
    # Save Cleaned Datasets
    # --------------------------------------------------

    http.to_csv("../dataset/http_clean.csv", index=False)
    logon.to_csv("../dataset/logon_clean.csv", index=False)
    device.to_csv("../dataset/device_clean.csv", index=False)
    file.to_csv("../dataset/file_clean.csv", index=False)
    email.to_csv("../dataset/email_clean.csv", index=False)

    print("\nCleaned Datasets Saved Successfully")
    print("../dataset/http_clean.csv")
    print("../dataset/logon_clean.csv")
    print("../dataset/device_clean.csv")
    print("../dataset/file_clean.csv")
    print("../dataset/email_clean.csv")

    return {
        "status": "success",
        "message": "Preprocessing Completed"
    }


if __name__ == "__main__":
    preprocess()