import pandas as pd
import time

def stream_csv(csv_file):

    print("=" * 60)
    print("CSV STREAM STARTED")
    print("=" * 60)

    data = pd.read_csv(csv_file)

    print(f"\nTotal Logs : {len(data)}")

    for index, row in data.iterrows():

        print(f"\nProcessing Log {index + 1}")

        yield row.to_dict()

        time.sleep(0.1)


if __name__ == "__main__":

    count = 0

    for row in stream_csv("../dataset/http_clean.csv"):

        print(row)

        count += 1

        if count == 5:
            break