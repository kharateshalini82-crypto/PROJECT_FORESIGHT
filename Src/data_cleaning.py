import pandas as pd
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
input_file = project_root / "data" / "raw" / "online_retail_II.csv"
output_file = project_root / "data" / "processed" / "cleaned_retail_data.csv"
df = pd.read_csv(input_file)
print("Original dataset shape:", df.shape)
duplicate_count = df.duplicated().sum()

print("Duplicate rows found:", duplicate_count)
df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)
missing_description = df["Description"].isnull().sum()

print("Missing Description values:", missing_description)
df["Description"] = df["Description"].fillna("Unknown Product")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print("InvoiceDate converted to datetime.")
df["Sales"] = df["Quantity"] * df["Price"]
invalid_quantity = (df["Quantity"] <= 0).sum()
print("Invalid quantity rows:", invalid_quantity)

df = df[df["Quantity"] > 0]
invalid_price = (df["Price"] <= 0).sum()

print("Invalid price rows:", invalid_price)

df = df[df["Price"] > 0]
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("Final shape:", df.shape)
print("Saved to:", output_file)