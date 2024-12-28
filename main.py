import yfinance as yf
import pandas as pd
from datetime import datetime

# Define the stock symbol and date range for the daily data
stock_symbol = "aapl"
start_date = "2023-04-01"
end_date = datetime.now().strftime("%Y-%m-%d")  # Use the current date as the end date

# Retrieve the daily stock data using yfinance
try:
    print("Fetching daily data...")
    daily_data = yf.download(stock_symbol, start=start_date, end=end_date, interval="1d")
    if daily_data.empty:
        raise ValueError("No data retrieved. Check the stock symbol or date range.")
    print("Daily data fetched successfully.")
except Exception as e:
    print(f"Error fetching daily data: {e}")
    exit()

# Keep only the 'Close' column
daily_data = daily_data[['Close']]

# Save daily data to a CSV file with stock name in the title
try:
    daily_file_name = f"{stock_symbol}_daily_prices.csv"
    daily_data.index = daily_data.index.strftime('%m/%d/%Y %H:%M:%S')  # Format date/time with military time
    daily_data.to_csv(daily_file_name)
    print(f"Daily prices saved to '{daily_file_name}'")
except Exception as e:
    print(f"Error saving daily prices: {e}")

# Retrieve the hourly stock data using yfinance, including extended hours
try:
    print("Fetching hourly data...")
    hourly_data = yf.download(stock_symbol, start=start_date, end=end_date, interval="1h", prepost=True)
    if hourly_data.empty:
        raise ValueError("No data retrieved for hourly data.")
    print("Hourly data fetched successfully.")
except Exception as e:
    print(f"Error fetching hourly data: {e}")
    exit()

# Keep only the 'Close' column
hourly_data = hourly_data[['Close']]

# Resample hourly data to 30-minute intervals
try:
    combined_data = hourly_data.resample('30T').ffill()
    print("Hourly data resampled successfully.")
    hourly_file_name = f"{stock_symbol}_hourly_prices.csv"
    combined_data.index = combined_data.index.strftime('%m/%d/%Y %H:%M:%S')  # Format date/time
    combined_data.to_csv(hourly_file_name)
    print(f"Hourly prices saved to '{hourly_file_name}'")
except Exception as e:
    print(f"Error resampling or saving hourly data: {e}")

# Filter and save trades taken between 10:00 AM and 2:30 PM to a CSV file
try:
    resampled_data = pd.read_csv(hourly_file_name, index_col=0, parse_dates=True)
    trades_within_trading_hours = resampled_data.between_time('10:00:00', '14:30:00')
    trades_file_name = f"{stock_symbol}_trades_within_trading_hours.csv"
    trades_within_trading_hours.to_csv(trades_file_name)
    print(f"Filtered trades saved to '{trades_file_name}'")
except Exception as e:
    print(f"Error filtering trades: {e}")

# Final message
print("Script execution completed!")
