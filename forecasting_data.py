import pandas as pd
from prophet import Prophet
from datetime import datetime

# Load your existing BTC data
df = pd.read_csv("data/BTC-USD_data.csv", parse_dates=["Date"])
df = df.rename(columns={"Date":"ds", "Close":"y"})[["ds","y"]]

# Train Prophet model
m = Prophet(interval_width=0.9)
m.fit(df)

# Forecast next 60 days
future = m.make_future_dataframe(periods=60)
forecast = m.predict(future)

# Save essential columns
forecast[["ds","yhat","yhat_lower","yhat_upper"]].to_csv("data/btc_forecast.csv", index=False)
