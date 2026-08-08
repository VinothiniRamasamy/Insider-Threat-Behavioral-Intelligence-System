import pandas as pd

# Read first 500 rows from HTTP dataset
df = pd.read_csv("../dataset/http_clean.csv", nrows=500)

# Save inside backend folder
df.to_csv("sample_logs.csv", index=False)

print("Sample CSV Created Successfully!")
print("Rows:", len(df))
print("Saved as: sample_logs.csv")