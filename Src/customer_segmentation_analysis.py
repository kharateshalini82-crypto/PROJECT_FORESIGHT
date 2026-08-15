import pandas as pd
import os

# ============================================================
# PROJECT FORESIGHT - CUSTOMER SEGMENTATION ANALYSIS
# ============================================================

input_file = "data/processed/feature_engineered_data.csv"

output_dir = "Outputs/Customer_Segmentation"

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
df["Customer ID"] = pd.to_numeric(df["Customer ID"], errors="coerce")

df = df.dropna(
    subset=["Customer ID", "Sales", "Quantity"]
)

print("\nCustomer data prepared successfully.")

# ============================================================
# 2. CUSTOMER-LEVEL SUMMARY
# ============================================================

customer_summary = (
    df.groupby("Customer ID")
    .agg(
        TotalSales=("Sales", "sum"),
        TotalQuantity=("Quantity", "sum"),
        TotalOrders=("Invoice", "nunique"),
        NumberOfProducts=("Description", "nunique")
    )
    .reset_index()
)

print(
    f"\nUnique customers analyzed: "
    f"{len(customer_summary)}"
)

# ============================================================
# 3. CUSTOMER SEGMENT
# ============================================================

# Use the existing CustomerSegment column
if "CustomerSegment" in df.columns:

    customer_segments = (
        df.groupby("Customer ID")["CustomerSegment"]
        .first()
        .reset_index()
    )

    customer_summary = customer_summary.merge(
        customer_segments,
        on="Customer ID",
        how="left"
    )

else:

    print(
        "\nCustomerSegment column not found."
    )

# ============================================================
# 4. SEGMENT SUMMARY
# ============================================================

if "CustomerSegment" in customer_summary.columns:

    segment_summary = (
        customer_summary
        .groupby("CustomerSegment")
        .agg(
            CustomerCount=("Customer ID", "nunique"),
            TotalSales=("TotalSales", "sum"),
            TotalQuantity=("TotalQuantity", "sum"),
            TotalOrders=("TotalOrders", "sum"),
            AverageCustomerSales=("TotalSales", "mean")
        )
        .reset_index()
    )

    # ========================================================
    # 5. SALES CONTRIBUTION
    # ========================================================

    total_sales = segment_summary["TotalSales"].sum()

    segment_summary["SalesContributionPercent"] = (
        segment_summary["TotalSales"]
        / total_sales
        * 100
    ).round(2)

    segment_summary["TotalSales"] = (
        segment_summary["TotalSales"].round(2)
    )

    segment_summary["AverageCustomerSales"] = (
        segment_summary["AverageCustomerSales"].round(2)
    )

    # ========================================================
    # 6. DISPLAY SEGMENT SUMMARY
    # ========================================================

    print(
        "\n========== CUSTOMER SEGMENT SUMMARY =========="
    )

    print(segment_summary)

    # ========================================================
    # 7. SAVE SEGMENT SUMMARY
    # ========================================================

    segment_summary.to_csv(
        f"{output_dir}/customer_segment_summary.csv",
        index=False
    )

# ============================================================
# 8. SAVE CUSTOMER DETAILS
# ============================================================

customer_summary["TotalSales"] = (
    customer_summary["TotalSales"].round(2)
)

customer_summary.to_csv(
    f"{output_dir}/customer_segment_details.csv",
    index=False
)

# ============================================================
# 9. FINAL OUTPUT
# ============================================================

print("\n==========================================")
print("CUSTOMER SEGMENTATION ANALYSIS COMPLETED!")
print("==========================================")

print(
    f"\nTotal customers analyzed: "
    f"{len(customer_summary)}"
)

print("\nFiles created:")

print(
    f"{output_dir}/customer_segment_summary.csv"
)

print(
    f"{output_dir}/customer_segment_details.csv"
)