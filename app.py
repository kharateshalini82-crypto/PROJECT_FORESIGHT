import streamlit as st
import pandas as pd
import os
from PIL import Image

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="PROJECT FORESIGHT",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 PROJECT FORESIGHT")
st.subheader("Sales Analytics, Customer Segmentation & Forecasting")

st.markdown("""
PROJECT FORESIGHT is an end-to-end business analytics project
that transforms retail transaction data into meaningful business
insights using Python, statistical forecasting and Power BI.
""")

st.divider()

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.header("📈 Key Business KPIs")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Sales", "20.48M")

with col2:
    st.metric("Customers", "5,878")

with col3:
    st.metric("Orders", "40,081")

with col4:
    st.metric("Quantity Sold", "11.2M")

with col5:
    st.metric("Average Order Value", "510.88")

st.divider()

# ---------------------------------------------------
# PROJECT WORKFLOW
# ---------------------------------------------------

st.header("🔄 Project Workflow")

st.markdown("""
**Raw Data → Data Cleaning → Feature Engineering → EDA →
Customer Segmentation → Product Analysis → Sales Forecasting →
Power BI Dashboard**
""")

st.divider()

# ---------------------------------------------------
# DASHBOARD PREVIEW
# ---------------------------------------------------

st.header("📊 Power BI Dashboard")

dashboard_path = "Outputs/Dashboard/dashboard_preview.png"

if os.path.exists(dashboard_path):
    image = Image.open(dashboard_path)
    st.image(
        image,
        caption="PROJECT FORESIGHT Sales Analytics Dashboard",
        use_container_width=True
    )
else:
    st.warning("Dashboard preview image not found.")

st.divider()

# ---------------------------------------------------
# EDA SECTION
# ---------------------------------------------------

st.header("📊 Exploratory Data Analysis")

eda_col1, eda_col2 = st.columns(2)

with eda_col1:

    path = "Outputs/EDA/monthly_sales_trend.png"

    if os.path.exists(path):
        st.image(
            path,
            caption="Monthly Sales Trend",
            use_container_width=True
        )

with eda_col2:

    path = "Outputs/EDA/sales_by_day.png"

    if os.path.exists(path):
        st.image(
            path,
            caption="Sales by Day",
            use_container_width=True
        )

eda_col3, eda_col4 = st.columns(2)

with eda_col3:

    path = "Outputs/EDA/top_10_products.png"

    if os.path.exists(path):
        st.image(
            path,
            caption="Top 10 Products",
            use_container_width=True
        )

with eda_col4:

    path = "Outputs/EDA/top_10_countries.png"

    if os.path.exists(path):
        st.image(
            path,
            caption="Top 10 Countries",
            use_container_width=True
        )

st.divider()

# ---------------------------------------------------
# CUSTOMER SEGMENTATION
# ---------------------------------------------------

st.header("👥 Customer Segmentation")

segment_path = "Outputs/customer_segments.csv"

if os.path.exists(segment_path):

    df_segments = pd.read_csv(segment_path)

    st.write("Customer segmentation results:")

    st.dataframe(
        df_segments.head(20),
        use_container_width=True
    )

else:

    st.info("Customer segmentation output is available in the project repository.")

st.divider()

st.header("🔮 Sales Forecast")

forecast_path = "Outputs/forecast_results.csv"

if os.path.exists(forecast_path):

    forecast_df = pd.read_csv(forecast_path)

    st.write("Forecast results:")

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

else:

    st.info("Forecast results are available in the project repository.")

st.divider()

st.header("🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Programming
    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    """)

with col2:
    st.markdown("""
    ### Analytics
    - Exploratory Data Analysis
    - Feature Engineering
    - Customer Segmentation
    - Product Analysis
    - Exponential Smoothing
    """)

with col3:
    st.markdown("""
    ### Tools
    - Microsoft Power BI
    - Visual Studio Code
    - Git
    - GitHub
    - Streamlit
    """)

st.divider()

# ---------------------------------------------------
# PROJECT OUTCOMES
# ---------------------------------------------------

st.header("🎯 Project Outcomes")

st.markdown("""
- Cleaned and prepared real-world retail transaction data
- Created analytical features for business analysis
- Identified sales trends and product performance
- Analyzed customer purchasing behavior
- Performed customer segmentation
- Forecasted future sales using Exponential Smoothing
- Developed an interactive Power BI dashboard
- Created a web-based analytics presentation using Streamlit
""")

st.divider()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.caption(
    "PROJECT FORESIGHT | Business Analytics Project | "
    "Shalini Prakash Kharate"
)