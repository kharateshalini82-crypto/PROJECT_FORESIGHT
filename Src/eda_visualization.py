import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# --------------------------------------------------
# 1. PROJECT PATH
# --------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

input_file = (
    project_root
    / "data"
    / "processed"
    / "cleaned_retail_data.csv"
)

output_folder = project_root / "Outputs" / "EDA"

output_folder.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

df = pd.read_csv(input_file, low_memory=False)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("Dataset loaded for visualization.")


# --------------------------------------------------
# 3. MONTHLY SALES TREND
# --------------------------------------------------

df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    output_folder / "monthly_sales_trend.png",
    dpi=150
)

plt.close()


# --------------------------------------------------
# 4. TOP 10 PRODUCTS
# --------------------------------------------------

top_products = (
    df.groupby("Description")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_products.index[::-1],
    top_products.values[::-1]
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")

plt.tight_layout()

plt.savefig(
    output_folder / "top_10_products.png",
    dpi=150
)

plt.close()


# --------------------------------------------------
# 5. TOP 10 COUNTRIES
# --------------------------------------------------

top_countries = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_countries.index[::-1],
    top_countries.values[::-1]
)

plt.title("Top 10 Countries by Sales")
plt.xlabel("Sales")

plt.tight_layout()

plt.savefig(
    output_folder / "top_10_countries.png",
    dpi=150
)

plt.close()


# --------------------------------------------------
# 6. SALES BY DAY
# --------------------------------------------------

day_sales = (
    df.groupby(df["InvoiceDate"].dt.day_name())["Sales"]
    .sum()
)

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_sales = day_sales.reindex(day_order)

plt.figure(figsize=(10, 6))

plt.bar(
    day_sales.index,
    day_sales.values
)

plt.title("Sales by Day of Week")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    output_folder / "sales_by_day.png",
    dpi=150
)

plt.close()


print("\nEDA visualizations created successfully!")

print("Saved charts to:")
print(output_folder)