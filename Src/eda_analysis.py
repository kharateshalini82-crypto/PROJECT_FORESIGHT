import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. PROJECT PATH
# --------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

input_file = project_root / "data" / "processed" / "cleaned_retail_data.csv"


# --------------------------------------------------
# 2. LOAD CLEANED DATA
# --------------------------------------------------

df = pd.read_csv(input_file)

# Convert InvoiceDate back to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


print("Cleaned dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# --------------------------------------------------
# 3. BUSINESS KPIs
# --------------------------------------------------

total_sales = df["Sales"].sum()

total_quantity = df["Quantity"].sum()

total_orders = df["Invoice"].nunique()

total_customers = df["Customer ID"].nunique()

average_order_value = total_sales / total_orders


print("\n========== BUSINESS KPIs ==========")

print("Total Sales:", round(total_sales, 2))

print("Total Quantity Sold:", total_quantity)

print("Total Orders:", total_orders)

print("Total Customers:", total_customers)

print("Average Order Value:", round(average_order_value, 2))


# --------------------------------------------------
# 4. TOP 10 PRODUCTS
# --------------------------------------------------

top_products = (
    df.groupby("Description")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS ==========")
print(top_products)


# --------------------------------------------------
# 5. TOP 10 COUNTRIES
# --------------------------------------------------

top_countries = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 COUNTRIES ==========")
print(top_countries)


# --------------------------------------------------
# 6. MONTHLY SALES
# --------------------------------------------------

df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)


# --------------------------------------------------
# 7. SALES BY COUNTRY
# --------------------------------------------------

country_sales = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY COUNTRY ==========")
print(country_sales.head(10))


# --------------------------------------------------
# 8. SALES BY DAY
# --------------------------------------------------

df["Day"] = df["InvoiceDate"].dt.day_name()

day_sales = (
    df.groupby("Day")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY DAY ==========")
print(day_sales)


# --------------------------------------------------
# 9. SAVE EDA RESULTS
# --------------------------------------------------

monthly_sales.to_csv(
    project_root / "data" / "processed" / "monthly_sales.csv"
)

top_products.to_csv(
    project_root / "data" / "processed" / "top_products.csv"
)

country_sales.to_csv(
    project_root / "data" / "processed" / "country_sales.csv"
)

print("\nEDA analysis completed successfully!")