import pandas as pd
import numpy as np
import os
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ============================================================
# PROJECT FORESIGHT - CUSTOMER SEGMENTATION
# RFM ANALYSIS + K-MEANS CLUSTERING
# ============================================================

input_file = "data/processed/feature_engineered_data.csv"

output_file = "Outputs/customer_segments.csv"
model_output = "Models/customer_segmentation_model.pkl"

print("Loading feature-engineered dataset...")

# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv(
    input_file,
    usecols=[
        "Invoice",
        "InvoiceDate",
        "Quantity",
        "Sales",
        "Customer ID"
    ]
)

print(f"Rows loaded: {len(df)}")

# ============================================================
# 2. PREPARE DATA
# ============================================================

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    errors="coerce"
)

# Remove records without Customer ID
df = df.dropna(
    subset=["Customer ID"]
)

# Keep only valid positive sales
df = df[
    (df["Sales"] > 0) &
    (df["Quantity"] > 0)
]

print(f"Rows after filtering: {len(df)}")

# ============================================================
# 3. SET ANALYSIS DATE
# ============================================================

analysis_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

print(f"Analysis date: {analysis_date.date()}")

# ============================================================
# 4. CREATE RFM FEATURES
# ============================================================

print("\nCreating RFM features...")

rfm = df.groupby("Customer ID").agg(
    Recency=(
        "InvoiceDate",
        lambda x: (analysis_date - x.max()).days
    ),
    Frequency=(
        "Invoice",
        "nunique"
    ),
    Monetary=(
        "Sales",
        "sum"
    )
).reset_index()

print(f"Customers identified: {len(rfm)}")

# ============================================================
# 5. DISPLAY RFM SUMMARY
# ============================================================

print("\n========== RFM SUMMARY ==========")

print(rfm[
    ["Recency", "Frequency", "Monetary"]
].describe())

# ============================================================
# 6. PREPARE DATA FOR K-MEANS
# ============================================================

rfm_model_data = rfm[
    ["Recency", "Frequency", "Monetary"]
].copy()

# Log transformation reduces the effect of extreme values
rfm_log = np.log1p(
    rfm_model_data
)

# Standardize features
scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(
    rfm_log
)

# ============================================================
# 7. K-MEANS CLUSTERING
# ============================================================

print("\nTraining K-Means customer segmentation model...")

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(
    rfm_scaled
)

print("K-Means clustering completed successfully.")

# ============================================================
# 8. ANALYZE CLUSTERS
# ============================================================

cluster_summary = rfm.groupby("Cluster").agg(
    Customers=("Customer ID", "count"),
    Avg_Recency=("Recency", "mean"),
    Avg_Frequency=("Frequency", "mean"),
    Avg_Monetary=("Monetary", "mean")
).round(2)

print("\n========== CLUSTER SUMMARY ==========")

print(cluster_summary)

# ============================================================
# 9. ASSIGN CUSTOMER SEGMENT NAMES
# ============================================================

# Rank clusters based on their RFM characteristics

cluster_summary["Score"] = (
    cluster_summary["Avg_Frequency"].rank(
        ascending=True
    )
    +
    cluster_summary["Avg_Monetary"].rank(
        ascending=True
    )
    +
    cluster_summary["Avg_Recency"].rank(
        ascending=False
    )
)

cluster_order = (
    cluster_summary["Score"]
    .sort_values(ascending=False)
    .index
)

segment_names = [
    "High Value Customers",
    "Loyal Customers",
    "Regular Customers",
    "Low Value Customers"
]

cluster_to_segment = {}

for cluster, segment in zip(
    cluster_order,
    segment_names
):
    cluster_to_segment[cluster] = segment

rfm["CustomerSegment"] = rfm["Cluster"].map(
    cluster_to_segment
)

# ============================================================
# 10. CUSTOMER SEGMENT SUMMARY
# ============================================================

segment_summary = rfm.groupby(
    "CustomerSegment"
).agg(
    Customers=("Customer ID", "count"),
    Avg_Recency=("Recency", "mean"),
    Avg_Frequency=("Frequency", "mean"),
    Avg_Monetary=("Monetary", "mean")
).round(2)

print("\n========== CUSTOMER SEGMENTS ==========")

print(segment_summary)

# ============================================================
# 11. SAVE CUSTOMER SEGMENTS
# ============================================================

os.makedirs(
    "Outputs",
    exist_ok=True
)

rfm.to_csv(
    output_file,
    index=False
)

# ============================================================
# 12. SAVE MODEL
# ============================================================

model_data = {
    "model": kmeans,
    "scaler": scaler
}

joblib.dump(
    model_data,
    model_output
)

# ============================================================
# 13. FINAL OUTPUT
# ============================================================

print("\n==========================================")
print("CUSTOMER SEGMENTATION COMPLETED SUCCESSFULLY!")
print("==========================================")

print(f"\nTotal Customers: {len(rfm)}")

print("\nCustomer Segment Distribution:")

print(
    rfm["CustomerSegment"]
    .value_counts()
)

print("\nCustomer segmentation saved to:")
print(output_file)

print("\nSegmentation model saved to:")
print(model_output)