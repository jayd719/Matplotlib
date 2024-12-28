import os
import yfinance as yf
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm
from ProcessResultsHTML import process_results
from datetime import datetime, timedelta
from Symbols import stocks

os.system("clear")
print("Performing Analysis")
# Initialize dataframe with default values
df = pd.DataFrame(columns=["Symbol", "3MH", "LastClose", "FilterOne"])


# Correction factor
CORRECTION_FACTOR = 0.10
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd


def calculate_slope(x_values, y_values):
    color = "r"
    x1, x2 = x_values
    y1, y2 = y_values
    slope = (y2 - y1) / ((x2 - x1).days)
    if slope > 0:
        color = "g"
    return color


def plot_last_15_day_slope(df: pd.DataFrame, plt: plt):
    x_values = [df.index[-15], df.index[-1]]
    y_values = [df["Close"].iloc[-15], df["Close"].iloc[-1]]
    color = calculate_slope(x_values, y_values)
    plt.plot(x_values, y_values, color=color)
    return color


def plot_threshold_lines(df: pd.DataFrame, plt: plt, delta=60):
    df_3m = df.iloc[-delta:]

    # Calculate the 3-month high and the last closing price
    three_month_max = df_3m["High"].max()
    last_close_price = df_3m["Close"].iloc[-1]

    # Compute the threshold price based on the correction factor
    threshold_price = three_month_max - (three_month_max * CORRECTION_FACTOR)
    threshold_price_2 = three_month_max - (three_month_max * (CORRECTION_FACTOR + 0.1))
    color, path = "r", "rejected"
    if last_close_price < threshold_price and last_close_price > threshold_price_2:
        color, path = "g", "accepted"
    elif last_close_price > threshold_price:
        color = "orange"
    # PLOT THRESHOLD LINE ONE
    plt.axhline(
        threshold_price,
        label=f"{CORRECTION_FACTOR} From High",
        color=color,
    )
    # PLOT THRESHOLD LINE TWO
    plt.axhline(
        threshold_price_2,
        label=f"{CORRECTION_FACTOR+.1} From High",
        color=color,
    )
    return color


def highlight_partition_max(df: pd.DataFrame, plt: plt, partitions=4):
    """
    Highlights the maximum 'High' values in each partition of the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing stock data with a 'High' column.
        plt (matplotlib.pyplot): Matplotlib plotting object.
        partitions (int): Number of partitions to divide the data into.
    """
    # Determine the size of each partition
    partition_size = len(df) // partitions
    max_values = []  # Store max 'High' values and their corresponding dates

    for i in range(partitions):
        # Create a partition of the DataFrame
        partition = df.iloc[i * partition_size : (i + 1) * partition_size]
        max_high = partition["High"].max()
        max_date = partition["High"].idxmax()

        # Store the max value and its date
        max_values.append((max_date, max_high))

        # Plot the max value and add a vertical line for partition start
        plt.plot(max_date, max_high, marker="o", label=f"Partition {i + 1}")
        plt.axvline(partition.index[0], linewidth=1, color="#bdbcbb")

    # Connect the max values with lines
    for i in range(1, len(max_values)):
        x_values = [max_values[i - 1][0], max_values[i][0]]
        y_values = [max_values[i - 1][1], max_values[i][1]]
        color = calculate_slope(x_values, y_values)
        plt.plot(
            x_values,
            y_values,
            linestyle="-.",
            color=color,
        )

    return color


def analyze_stock(symbol: str, analysis_date=datetime.today(), days=365):
    """
    Analyzes a stock's historical data and plots its performance.

    Args:
        symbol (str): The stock symbol (e.g., "AAPL").
        analysis_date (datetime): The end date for analysis (default: today).
    """
    # Fetch historical data for the stock
    stock = yf.Ticker(symbol)
    start_date = analysis_date - timedelta(days=days)
    stock_data = stock.history(start=start_date, end=analysis_date)

    # Configure plot aesthetics
    plt.style.use("fivethirtyeight")
    plt.figure(figsize=(15, 8))
    plt.grid(axis="x")

    # Highlight max values in partitions
    c1 = highlight_partition_max(df=stock_data, plt=plt)
    # Threshold Line
    c2 = plot_threshold_lines(stock_data, plt)
    c3 = plot_last_15_day_slope(stock_data, plt)

    color = "b"
    if c1 == c2 and c2 == c3:
        color = c1
    # Plot the 'High' price over time
    plt.plot(stock_data.index, stock_data["High"], label="High Price", color=color)

    # Add plot labels and legend
    plt.legend()
    plt.title(f"Stock Analysis for {symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.tight_layout()
    # plt.show()
    plt.savefig(f"plots/STOCKS/{color}/{symbol}.png")
    plt.close()


# Example usage
if __name__ == "__main__":
    # analyze_stock("AAPL")
    for stock in tqdm(stocks):
        analyze_stock(stock)

    # Display the final dataframe
    # print(df)
    process_results(src="plots/STOCKS/")
