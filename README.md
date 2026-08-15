# PROJECT FORESIGHT
## AI-Powered Demand & Inventory Intelligence Platform

### Project Overview

PROJECT FORESIGHT is a business analytics project designed to analyze retail sales data, identify important sales and customer patterns, perform customer segmentation and product analysis, and forecast future sales.

The project combines Python-based data analytics, statistical forecasting, and Microsoft Power BI to transform retail transaction data into meaningful business insights.

---

## Objectives

- Analyze historical retail sales performance.
- Clean and prepare retail transaction data.
- Perform exploratory data analysis.
- Identify important sales trends.
- Analyze product performance.
- Analyze sales by country.
- Perform customer segmentation.
- Forecast future sales.
- Develop an interactive Power BI dashboard.
- Support data-driven business decision-making.

---

## Dataset

The project uses the Online Retail II transaction dataset.

The dataset contains retail transaction information including:

- Invoice information
- Product descriptions
- Quantity
- Invoice date
- Unit price
- Customer ID
- Country

The original and processed datasets are maintained locally because of their large file sizes.

---

## Project Structure

```text
PROJECT_FORESIGHT/
│
├── Models/
│   ├── customer_segmentation.py
│   ├── customer_segmentation_model.pkl
│   ├── forecast_model.pkl
│   └── sales_forecasting.py
│
├── Outputs/
│   ├── Customer_Segmentation/
│   ├── EDA/
│   ├── Product_Analysis/
│   ├── customer_segments.csv
│   └── forecast_results.csv
│
├── Src/
│   ├── customer_segmentation_analysis.py
│   ├── data_cleaning.py
│   ├── data_understanding.py
│   ├── eda_analysis.py
│   ├── eda_visualization.py
│   ├── feature_engineering.py
│   └── product_analysis.py
│
├── PowerBI/
├── Dashboard/
├── notebooks/
├── Sql/
├── data/
│
├── .gitignore
└── requirements.txt
