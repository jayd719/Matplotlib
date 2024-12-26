"""-------------------------------------------------------
Matplot Lib: Module Description Here
-------------------------------------------------------
Author:  JD
ID:      91786
Project: Data Analysis
Version:  1.0.8
__updated__ = Thu Dec 26 2024
-------------------------------------------------------
"""

import pandas as pd
from matplotlib import pyplot as plt


# Read Data from CSV file using pandas
data = pd.read_csv("data/data2.csv")

# bins
bins = []

min = data["Age"].min()
max = data["Age"].max()
currAge = 0
while currAge < max:
    currAge += 5
    bins.append(currAge)


# Set theme and size of plot
plt.style.use("fivethirtyeight")
plt.figure(figsize=(12, 8))

# Set Lables and Title
plt.title("Ages of Respondents")
plt.xlabel("Ages")
plt.ylabel("Number Of Respondents")

# Plot Histogram
plt.hist(data["Age"], edgecolor="k", bins=bins, log=True)

# Caluculate mode,medain, and mean
mean = data["Age"].mean()
median = data["Age"].median()
mode = data["Age"].mode()

# Plot mode,median and mean
plt.axvline(median, label="Median", color="r", linestyle="--")
plt.axvline(mean, label="Mean", color="k", linestyle="-")
plt.axvline(mode.iloc[0], label="Mode", color="y")

plt.legend()
plt.tight_layout()
plt.savefig("plots/histogram.png")
plt.show()
