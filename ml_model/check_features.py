import pandas as pd

print("Loading Dataset...")

data = pd.read_csv("../dataset/final_features.csv")

print("Dataset Loaded Successfully")

print("\nFeatures in Dataset:")
print(data.columns.tolist())