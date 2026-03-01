import yfinance as yf
import pandas as pd
from pathlib import Path

print("📥 Downloading full BTC-USD historical data...")

# Fetch full history — start from 2014 (Bitcoin has data from then)
df = yf.download("BTC-USD", start="2014-01-01", end="2025-10-30", interval="1d", auto_adjust=True)

# Check results
print("✅ Download complete.")
print("Rows fetched:", len(df))
print(df.head())

# Handle empty data
if df.empty:
    print("⚠️ No data fetched! Please check your network or try again later.")
else:
    Path("data").mkdir(exist_ok=True)
    df.reset_index().to_csv("data/BTC-USD_data.csv", index=False)
    print(f"✅ Full dataset saved successfully ({len(df)} rows) in 'data/BTC-USD_data.csv'")
