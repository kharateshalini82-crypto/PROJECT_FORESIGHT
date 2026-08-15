import pandas as pd
import os

# ============================================================
# PROJECT FORESIGHT - PRODUCT ANALYSIS
# ============================================================

input_file = "data/processed/feature_engineered_data.csv"

output_dir = "Outputs/Product_Analysis"

os.makedirs(output_dir, exist_ok=True)

print("Loading feature-engineered dataset...")

df = pd.read_csv(input_file)

print(f"Rows loaded: {len(df)}")
print(f"Columns loaded: {len(df.columns)}")

# ============================================================
# 1. PREPARE DATA
# ============================================================

df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

df["Description"] = df["Description"].astype(str).str.strip()

df = df.dropna(subset=["Description", "Sales", "Quantity"])

print("\nProduct data prepared successfully.")

# ============================================================
# 2. PRODUCT SALES ANALYSIS
# ============================================================

product_sales = (
    df.groupby("Description")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

product_sales.columns = ["Product", "TotalSales"]

product_sales["TotalSales"] = product_sales["TotalSales"].round(2)

# Product sales rank
product_sales["SalesRank"] = range(1, len(product_sales) + 1)

# ============================================================
# 3. PRODUCT QUANTITY ANALYSIS
# ============================================================

product_quantity = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

product_quantity.columns = ["Product", "TotalQuantity"]

# ============================================================
# 4. COMBINE PRODUCT PERFORMANCE
# ============================================================

product_performance = pd.merge(
    product_sales,
    product_quantity,
    on="Product",
    how="left"
)

# ============================================================
# 5. SALES CONTRIBUTION
# ============================================================

total_sales = product_performance["TotalSales"].sum()

product_performance["SalesContributionPercent"] = (
    product_performance["TotalSales"] / total_sales * 100
).round(2)

# ============================================================
# 6. TOP 10 PRODUCTS BY SALES
# ============================================================

top_10_products = product_performance.head(10)

print("\n========== TOP 10 PRODUCTS BY SALES ==========")

print(top_10_products)

# ============================================================
# 7. TOP 10 PRODUCTS BY QUANTITY
# ============================================================

top_10_quantity = (
    product_performance
    .sort_values("TotalQuantity", ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS BY QUANTITY ==========")

print(top_10_quantity)

# ============================================================
# 8. SAVE PRODUCT PERFORMANCE
# ============================================================

product_performance.to_csv(
    f"{output_dir}/product_performance.csv",
    index=False
)

# ============================================================
# 9. SAVE TOP 10 PRODUCTS
# ============================================================

top_10_products.to_csv(
    f"{output_dir}/top_10_products.csv",
    index=False
)

# ============================================================
# 10. SAVE TOP 10 BY QUANTITY
# ============================================================

top_10_quantity.to_csv(
    f"{output_dir}/top_10_quantity.csv",
    index=False
)

# ============================================================
# 11. FINAL OUTPUT
# ============================================================

print("\n==========================================")
print("PRODUCT ANALYSIS COMPLETED SUCCESSFULLY!")
print("==========================================")

print(f"\nTotal unique products: {len(product_performance)}")

print("\nFiles created:")

print(f"{output_dir}/product_performance.csv")
print(f"{output_dir}/top_10_products.csv")
print(f"{output_dir}/top_10_quantity.csv")