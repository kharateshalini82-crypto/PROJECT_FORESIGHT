import pandas as pd
import os
input_file = "data/processed/cleaned_retail_data.csv"
output_file = "data/processed/feature_engineered_data.csv"

print("Loading cleaned dataset...")
df = pd.read_csv(input_file)
print(f"Rows loaded: {len(df)}")
print(f"Columns loaded: {len(df.columns)}")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print("InvoiceDate converted successfully.")
df["Sales"] = df["Quantity"] * df["Price"]
print("Sales feature created.")
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["MonthName"] = df["InvoiceDate"].dt.month_name()
df["Quarter"] = df["InvoiceDate"].dt.quarter
df["Day"] = df["InvoiceDate"].dt.day
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()

df["IsWeekend"] = df["InvoiceDate"].dt.dayofweek >= 5

print("Time-based features created.")
df["IsCancelled"] = df["Invoice"].astype(str).str.startswith("C")
print("Cancellation feature created.")
customer_sales = df.groupby("Customer ID")["Sales"].sum()
def customer_segment(value):
    if value >= 5000:
        return "High Value"
    elif value >= 1000:
        return "Medium Value"
    else:
        return "Low Value"

customer_segments = customer_sales.apply(customer_segment)
df["CustomerSegment"] = df["Customer ID"].map(customer_segments)
print("Customer segmentation created.")
product_sales = df.groupby("Description")["Sales"].sum()
product_rank = product_sales.rank(
    method="dense",
    ascending=False
)
df["ProductSalesRank"] = df["Description"].map(product_rank)
print("Product ranking created.")
os.makedirs("data/processed", exist_ok=True)
df.to_csv(output_file, index=False)
print("\n==========================================")
print("FEATURE ENGINEERING COMPLETED SUCCESSFULLY!")
print("==========================================")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("\nNew Features:")
print([
    "Sales",
    "Year",
    "Month",
    "MonthName",
    "Quarter",
    "Day",
    "DayOfWeek",
    "IsWeekend",
    "IsCancelled",
    "CustomerSegment",
    "ProductSalesRank"
])
print(f"\nSaved to: {output_file}")