Stock historical data
Used for backtesting stock strategies

This Python script automates the process of downloading, processing, and saving stock price data for Apple (AAPL) using the yfinance and pandas libraries. Here’s a summary of its main steps:

Fetch Daily Data:
Downloads daily closing prices for AAPL from April 1, 2023, to today.
Saves this data to a CSV file named aapl_daily_prices.csv.

Fetch Hourly Data:
Downloads hourly closing prices for AAPL, including extended trading hours, over the same date range.
Resamples this hourly data into 30-minute intervals and saves it as aapl_hourly_prices.csv.

Filter Trading Hours:
Loads the resampled data and filters it to include only trades between 10:00 AM and 2:30 PM.
Saves the filtered data to a file named aapl_trades_within_trading_hours.csv.

Error Handling:
Handles errors at each stage (downloading, saving, resampling, filtering) and prints informative messages if anything fails.

Formatting:
Formats date and time in the output CSVs using the format mm/dd/yyyy HH:MM:SS (military time).

In summary:
The script downloads AAPL stock data at daily and hourly resolutions, processes and formats it, filters for trades during specific hours, and saves the results to CSV files, with robust error handling throughout.
