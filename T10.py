import os
import yfinance as yf
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm
from ProcessResultsHTML import process_results

os.system("clear")
print("Performing Analysis")
# Initialize dataframe with default values
df = pd.DataFrame(columns=["Symbol", "3MH", "LastClose", "FilterOne"])

# List of stock symbols
stocks = [
    "MSFT",
    "AAPL",
    "GOOGL",
    "AMZN",
    "TSLA",
    "META",
    "NVDA",
    "NFLX",
    "INTC",
    "AMD",
    "SPY",
    "MSCI",
    "DIS",
    "BA",
    "IBM",
    "V",
    "MA",
    "JNJ",
    "PFE",
    "MRK",
    "GS",
    "WMT",
    "KO",
    "PEP",
    "UNH",
    "JPM",
    "XOM",
    "CVX",
    "MCD",
    "COST",
    "LMT",
]

# Correction factor
CORRECTION_FACTOR = 0.10

# Loop over each stock symbol
for stock in tqdm(stocks):
    # Fetch stock data for the last 3 months
    ticker = yf.Ticker(stock)
    stock_data = ticker.history(period="1y")
    stock_data_3m = ticker.history(period="3mo")

    # Calculate the 3-month high and the last closing price
    three_month_max = stock_data_3m["High"].max()
    last_close_price = stock_data_3m["Close"].iloc[-1]

    # Compute the threshold price based on the correction factor
    threshold_price = three_month_max - (three_month_max * CORRECTION_FACTOR)
    threshold_price_2 = three_month_max - (three_month_max * (CORRECTION_FACTOR + 0.1))
    color, path = "r", "rejected"
    if last_close_price < threshold_price and last_close_price > threshold_price_2:
        color, path = "g", "accepted"
    elif last_close_price > threshold_price:
        color = "y"

    # PLOT SETTINGS
    plt.style.use("bmh")
    plt.figure(figsize=(12, 5))
    plt.plot(stock_data.index, stock_data["Close"], label="Closing Price", color=color)

    # PLOT THRESHOLD LINE ONE
    plt.axhline(
        threshold_price,
        label=f"{CORRECTION_FACTOR} From High",
        color="y",
        linestyle="-.",
    )
    # PLOT THRESHOLD LINE TWO
    plt.axhline(
        threshold_price_2,
        label=f"{CORRECTION_FACTOR+.1} From High",
        color="r",
        linestyle="-.",
    )
    plt.title(f"Stock Prices for {stock}", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend(loc="best")
    plt.savefig(f"plots/STOCKS/{path}/{stock}.png")
    plt.close()

# Display the final dataframe
# print(df)
process_results(src="plots/STOCKS/")
