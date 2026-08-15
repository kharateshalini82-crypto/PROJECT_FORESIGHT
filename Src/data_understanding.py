import pandas as pd
from pathlib import Path

# Get the main PROJECT_FORESIGHT folder
project_root = Path(__file__).resolve().parent.parent

# Dataset location
file_path = project_root / "data" / "raw" / "online_retail_II.csv"

# Load dataset
df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())