import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATH
# --------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

input_file = project_root / "data" / "raw" / "online_retail_II.csv"

output_file = project_root / "data" / "processed" / "cleaned_retail_data.csv"


# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)


# --------------------------------------------------
# 3. REMOVE DUPLICATES
# --------------------------------------------------

duplicate_count = df.duplicated().sum()

print("Duplicate rows found:", duplicate_count)

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)


# --------------------------------------------------
# 4. HANDLE MISSING DESCRIPTIONS
# --------------------------------------------------

missing_description = df["Description"].isnull().sum()

print("Missing Description values:", missing_description)

df["Description"] = df["Description"].fillna("Unknown Product")


# --------------------------------------------------
# 5. CONVERT INVOICE DATE
# --------------------------------------------------

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("InvoiceDate converted to datetime.")


# --------------------------------------------------
# 6. CREATE SALES AMOUNT
# --------------------------------------------------

df["Sales"] = df["Quantity"] * df["Price"]


# --------------------------------------------------
# 7. REMOVE INVALID QUANTITIES
# --------------------------------------------------

invalid_quantity = (df["Quantity"] <= 0).sum()

print("Invalid quantity rows:", invalid_quantity)

df = df[df["Quantity"] > 0]


# --------------------------------------------------
# 8. REMOVE INVALID PRICES
# --------------------------------------------------

invalid_price = (df["Price"] <= 0).sum()

print("Invalid price rows:", invalid_price)

df = df[df["Price"] > 0]


# --------------------------------------------------
# 9. SAVE CLEANED DATA
# --------------------------------------------------

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("Final shape:", df.shape)
print("Saved to:", output_file)