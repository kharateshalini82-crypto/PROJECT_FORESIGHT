import pandas as pd
import numpy as np
import os

from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error
input_file = "data/processed/feature_engineered_data.csv"

forecast_output = "Outputs/forecast_results.csv"
model_output = "Models/forecast_model.pkl"


print("Loading feature-engineered dataset...")

df = pd.read_csv(input_file)

print(f"Rows loaded: {len(df)}")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

monthly_sales = (
    df.groupby(df["InvoiceDate"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["InvoiceDate"] = monthly_sales["InvoiceDate"].dt.to_timestamp()

monthly_sales = monthly_sales.sort_values("InvoiceDate")

monthly_sales = monthly_sales.set_index("InvoiceDate")

monthly_sales = monthly_sales.asfreq("MS")

print("\nMonthly sales data prepared.")

print(f"Number of months: {len(monthly_sales)}")

print("\n========== HISTORICAL MONTHLY SALES ==========")

print(monthly_sales)

train = monthly_sales.iloc[:-1]

test = monthly_sales.iloc[-1:]

print("\n========== TRAIN / TEST SPLIT ==========")

print(f"Training months: {len(train)}")
print(f"Testing months: {len(test)}")

print("\nTraining Holt-Winters forecasting model...")

model = ExponentialSmoothing(
    train["Sales"],
    trend="add",
    seasonal="add",
    seasonal_periods=12
)

fitted_model = model.fit(
    optimized=True
)

print("Forecasting model trained successfully.")

test_predictions = fitted_model.forecast(len(test))

test_predictions.index = test.index

mae = mean_absolute_error(
    test["Sales"],
    test_predictions
)

rmse = np.sqrt(
    mean_squared_error(
        test["Sales"],
        test_predictions
    )
)

mape = np.mean(
    np.abs(
        (test["Sales"] - test_predictions)
        / test["Sales"]
    )
) * 100


print("\n========== MODEL EVALUATION ==========")

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"MAPE : {mape:.2f}%")
print("\nTraining final model on complete dataset...")

final_model = ExponentialSmoothing(
    monthly_sales["Sales"],
    trend="add",
    seasonal="add",
    seasonal_periods=12
)

final_fitted_model = final_model.fit(
    optimized=True
)
forecast_periods = 6

future_forecast = final_fitted_model.forecast(
    forecast_periods
)

print("\n========== FUTURE SALES FORECAST ==========")

print(future_forecast)

forecast_df = future_forecast.reset_index()

forecast_df.columns = [
    "ForecastMonth",
    "ForecastSales"
]

forecast_df["ForecastMonth"] = pd.to_datetime(
    forecast_df["ForecastMonth"]
)

forecast_df["ForecastSales"] = forecast_df[
    "ForecastSales"
].round(2)

os.makedirs("Outputs", exist_ok=True)

forecast_df.to_csv(
    forecast_output,
    index=False
)
import joblib

joblib.dump(
    final_fitted_model,
    model_output
)
print("\n==========================================")
print("FORECASTING COMPLETED SUCCESSFULLY!")
print("==========================================")

print("\nModel: Holt-Winters Exponential Smoothing")

print(f"\nMAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"MAPE : {mape:.2f}%")

print("\nNext 6 Months Forecast:")

print(forecast_df)

print(f"\nForecast saved to:")
print(forecast_output)

print(f"\nModel saved to:")
print(model_output)