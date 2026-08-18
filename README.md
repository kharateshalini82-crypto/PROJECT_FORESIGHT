
# PROJECT FORESIGHT

## Sales Analytics, Customer Segmentation & Forecasting Project

## Project Overview

PROJECT FORESIGHT is a business analytics project where I worked on real retail transaction data to find useful business insights.

In this project, I used Python to clean and analyze the data, understand patterns, group customers, study product performance, and also predict future sales. I also used Power BI to create an interactive dashboard that shows important business metrics like sales, customers, and trends in a visual way.

The whole project follows a step-by-step process:

**Raw Data → Data Cleaning → Feature Creation → Data Analysis → Customer Segmentation → Product Analysis → Sales Forecasting → Power BI Dashboard**

## Objectives

The main goals of this project were:

* To study past sales data and understand business performance
* To clean and prepare raw retail data for analysis
* To explore the data and find useful patterns
* To identify sales trends over time
* To analyze which products perform best
* To understand sales across different countries
* To group customers based on their buying behavior
* To predict future sales using forecasting techniques
* To calculate important business KPIs
* To build a Power BI dashboard for visualization
* To support better business decision-making using data

## Dataset

For this project, I used the **Online Retail II dataset**, which contains real retail transaction data.

It includes details like:

* Invoice number
* Product name
* Quantity purchased
* Invoice date
* Price of each item
* Customer ID
* Country

The dataset was quite large, with around **1,067,371 rows** initially. After cleaning the data and removing errors or missing values, around **1,007,914 rows** were used for analysis.

Because the dataset is very large, I did not upload the raw files to GitHub. Instead, I included only the cleaned code, outputs, models, and dashboard files.

## Key Business KPIs

| KPI                 |         Value |
| ------------------- | ------------: |
| Total Sales         | 20,476,634.02 |
| Total Quantity Sold |    11,205,149 |
| Total Orders        |        40,081 |
| Total Customers     |         5,878 |
| Average Order Value |        510.88 |

## Key Features of the Project

### 1. Data Cleaning

I cleaned the raw dataset using Python and Pandas. This included fixing missing values, removing incorrect records, and preparing the data for analysis.

### 2. Feature Engineering

I created new useful columns to improve analysis, such as:

* Sales value
* Year, Month, Quarter
* Day and Day of Week
* Weekend indicator
* Cancelled order flag
* Customer segments
* Product ranking

### 3. Exploratory Data Analysis (EDA)

I explored the data to understand:

* How sales change over time
* Which days have higher sales
* Best-selling products
* Sales by country
* Customer buying behavior
* Overall transaction patterns

### 4. Customer Segmentation

I grouped customers based on their purchasing behavior. This helps in understanding different types of customers and how they contribute to sales.

### 5. Product Analysis

I analyzed products to find:

* Top-selling products
* Products with high quantity sales
* Overall product performance

### 6. Sales Forecasting

I used past sales data to predict future sales.

For forecasting, I used **Exponential Smoothing**, which helps in understanding future trends based on historical data.

## Power BI Dashboard

I also created an interactive dashboard using Microsoft Power BI.

This dashboard shows:

* Total Sales
* Total Customers
* Total Orders
* Total Quantity Sold
* Average Order Value
* Monthly sales trends
* Sales by product
* Sales by country
* Sales forecast

## Technology Used

### Programming Language

* Python

### Python Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Statsmodels

### Visualization Tool

* Microsoft Power BI

### Tools Used

* Git
* GitHub
* Visual Studio Code

## Project Structure

* **Models** → Machine learning and forecasting files
* **Outputs** → Results like charts, CSV files, and analysis outputs
* **Src** → All Python scripts for analysis
* **PowerBI** → Power BI dashboard file
* **Data** → Dataset (not uploaded due to size)

## Forecasting Output

* Forecast results: `Outputs/forecast_results.csv`
* Trained model: `Models/forecast_model.pkl`

## Project Results

This project produced:

* Customer segmentation results
* Product performance insights
* Sales trend analysis
* Country-wise sales insights
* Forecasted future sales
* Visual dashboards for business understanding

## Project Workflow

**Dataset → Understanding → Cleaning → Feature Creation → Analysis → Segmentation → Product Study → Forecasting → Dashboard → Insights**

## Key Outcomes

From this project, I was able to:

* Clean and prepare real-world retail data
* Create useful features for analysis
* Understand customer behavior
* Identify top products and sales trends
* Predict future sales
* Build a professional Power BI dashboard
* Organize the project in a structured way using GitHub

## Limitations

* Forecasting is based only on past data
* External factors like market changes are not included
* Results are estimates, not exact future values
* Accuracy depends on historical patterns

## Future Improvements

* Using more advanced forecasting models
* Adding real-time data updates
* Building a web-based dashboard
* Adding product recommendation system
* Detecting unusual sales patterns
* Automating dashboard updates

## Conclusion

PROJECT FORESIGHT shows how raw retail data can be turned into useful business insights.

By combining Python, data analysis, forecasting, and Power BI, I was able to build a complete end-to-end analytics project.

This project helps understand sales trends, customer behavior, product performance, and future sales predictions in a simple and visual way.

## Repository

GitHub Link:
https://github.com/kharateshalini82-crypto/PROJECT_FORESIGHT


## Project Details

* Project Name: PROJECT FORESIGHT
* Student: Shalini Prakash Kharate & Komal Bhausaheb Jadhav
* Domain: Business Analytics
* Dataset: Online Retail II
* Forecasting Method: Exponential Smoothing
* Visualization Tool: Power BI
* Version Control: Git & GitHub
