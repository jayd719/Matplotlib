import os
import yfinance as yf
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm
from ProcessResultsHTML import process_results
from datetime import datetime, timedelta
from Symbols import stocks

# Constants
CORRECTION_FACTOR = 0.10
PLOT_SAVE_PATH = "plots/STOCKS/b"
PARTITIONS = 4
DAYS_ANALYSIS = 365


def clear_console():
    """Clear the console output."""
    os.system("clear")
    print("Performing Analysis")


def plot_candle_chart(df):
    """Plots a candlestick chart for the stock data."""
    green_candles = df[df["Close"] >= df["Open"]]
    red_candles = df[df["Close"] < df["Open"]]

    # Green candles
    plt.bar(
        green_candles.index,
        green_candles["Close"] - green_candles["Open"],
        bottom=green_candles["Open"],
        color="g",
    )
    plt.bar(
        green_candles.index,
        green_candles["High"] - green_candles["Low"],
        bottom=green_candles["Low"],
        color="g",
        width=0.15,
    )

    # Red candles
    plt.bar(
        red_candles.index,
        red_candles["Open"] - red_candles["Close"],
        bottom=red_candles["Close"],
        color="r",
    )
    plt.bar(
        red_candles.index,
        red_candles["High"] - red_candles["Low"],
        bottom=red_candles["Low"],
        color="r",
        width=0.15,
    )


def calculate_slope(x_values, y_values):
    """Calculate the slope and determine the line color."""
    x1, x2 = x_values
    y1, y2 = y_values
    slope = (y2 - y1) / ((x2 - x1).days)
    return "g" if slope > 0 else "r"


def plot_last_15_day_slope(df):
    """Plot the slope of the last 15 days."""
    x_values = [df.index[-15], df.index[-1]]
    y_values = [df["Close"].iloc[-15], df["Close"].iloc[-1]]
    color = calculate_slope(x_values, y_values)
    plt.plot(x_values, y_values, color=color, linewidth=1.4)


def plot_threshold_lines(df, delta=60):
    """Plot threshold lines based on a correction factor."""
    recent_data = df.iloc[-delta:]
    three_month_max = recent_data["High"].max()
    last_close_price = recent_data["Close"].iloc[-1]

    threshold_1 = three_month_max - (three_month_max * CORRECTION_FACTOR)
    threshold_2 = three_month_max - (three_month_max * (CORRECTION_FACTOR + 0.1))

    color = (
        "#99ff99"
        if last_close_price < threshold_1
        else ("#ff9999" if last_close_price > threshold_2 else "#a3a3c2")
    )

    plt.axhline(
        threshold_1,
        label=f"{CORRECTION_FACTOR}% From 3-Month High",
        color=color,
        linewidth=1.4,
    )
    plt.axhline(
        threshold_2,
        label=f"{CORRECTION_FACTOR + 0.1}% From 3-Month High",
        color=color,
        linewidth=1.4,
    )
    plt.fill_between(df.index, threshold_2, threshold_1, color=color)


def plot_quarters(df, partitions=PARTITIONS):
    """Highlight maximum 'High' values in each partition of the DataFrame."""
    partition_size = len(df) // partitions
    max_values = []

    for i in range(partitions):
        partition = df.iloc[i * partition_size : (i + 1) * partition_size]
        max_high = partition["High"].max()
        max_date = partition["High"].idxmax()
        max_values.append((max_date, max_high))

        plt.plot(max_date, max_high, marker="o", color="#00cc00")
        plt.axvline(partition.index[0], color="#bdbcbb", linestyle="--", linewidth=0.75)

    for i in range(1, len(max_values)):
        x_values = [max_values[i - 1][0], max_values[i][0]]
        y_values = [max_values[i - 1][1], max_values[i][1]]
        color = calculate_slope(x_values, y_values)
        plt.plot(x_values, y_values, linestyle="-.", color=color, linewidth=1.4)


def analyze_stock(symbol, analysis_date=datetime.today(), days=DAYS_ANALYSIS):
    """Fetch and analyze stock data, then generate plots."""
    stock = yf.Ticker(symbol)
    start_date = analysis_date - timedelta(days=days)
    stock_data = stock.history(start=start_date, end=analysis_date)

    plt.style.use("fivethirtyeight")
    plt.figure(figsize=(15, 8))
    plt.grid(False)

    plot_quarters(stock_data)
    plot_threshold_lines(stock_data)
    plot_last_15_day_slope(stock_data)
    plot_candle_chart(stock_data)

    plt.legend()
    plt.title(f"Stock Analysis for {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig(f"{PLOT_SAVE_PATH}{symbol}.png")
    plt.close()


def main():
    clear_console()
    analyze_stock("AAPL")
    for stock in tqdm(stocks, desc="Performing Analysis One"):
        analyze_stock(stock)
    process_results(src="plots/STOCKS/")


if __name__ == "__main__":
    main()
