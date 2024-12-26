"""-------------------------------------------------------
Matplotlib: 
This code visualizes the median salaries of all developers and Python developers
across ages using Matplotlib. It plots salary data, highlights areas where Python 
developer salaries exceed or fall below all developers', and customizes the plot 
with a professional theme, labels, and a legend for better readability and presentation
-------------------------------------------------------
Author:  JD
ID:      91786
Project: Data Analysis
Version:  1.0.8
__updated__ = Thu Dec 26 2024
-------------------------------------------------------
"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

ages_x = np.array(
    [
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
    ]
)

py_dev_y = np.array(
    [
        20046,
        17100,
        20000,
        24744,
        30500,
        37732,
        41247,
        45372,
        48876,
        45000,
        50287,
        50016,
        50998,
        70003,
        70000,
        71496,
        75370,
        83640,
        84666,
        84392,
        78254,
        85000,
        87038,
        91991,
        100000,
        94796,
        97962,
        93302,
        99240,
        102736,
        112285,
        100771,
        104708,
        108423,
        101407,
        112542,
        122870,
        120000,
    ]
)

js_dev_y = np.array(
    [
        16446,
        16791,
        18942,
        21780,
        25704,
        29000,
        34372,
        37810,
        43515,
        46823,
        49293,
        53437,
        56373,
        62375,
        66674,
        68745,
        68746,
        74583,
        79000,
        78508,
        79996,
        80403,
        83820,
        88833,
        91660,
        87892,
        96243,
        90000,
        99313,
        91660,
        102264,
        100000,
        100000,
        91660,
        99240,
        108000,
        105000,
        104000,
    ]
)

dev_y = np.array(
    [
        17784,
        16500,
        18012,
        20628,
        25206,
        30252,
        34368,
        38496,
        42000,
        46752,
        49320,
        53200,
        56000,
        62316,
        64928,
        67317,
        68748,
        73752,
        77232,
        78000,
        78508,
        79536,
        82488,
        88935,
        90000,
        90056,
        95000,
        90000,
        91633,
        91660,
        98150,
        98964,
        100000,
        98988,
        100000,
        108923,
        105000,
        103117,
    ]
)
# Set the plot style and figure size
plt.style.use("ggplot")
plt.figure(figsize=(12, 8))

# Add title and axis labels
plt.title("Median Salaries", fontsize=16)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Median Salary", fontsize=12)

# Plot data for all developers
plt.plot(
    ages_x,
    dev_y,
    label="All Developers",
    linestyle="--",
    linewidth=2,
)

# Plot data for Python developers
plt.plot(
    ages_x,
    py_dev_y,
    label="Python Developers",
    linewidth=2,
)

# Highlight areas where Python dev salaries are greater or less than all dev salaries
plt.fill_between(
    ages_x,
    py_dev_y,
    dev_y,
    where=(py_dev_y >= dev_y),
    interpolate=True,
    alpha=0.5,
    color="green",
    label="Above All Devs",
)

plt.fill_between(
    ages_x,
    py_dev_y,
    dev_y,
    where=(py_dev_y < dev_y),
    interpolate=True,
    alpha=0.5,
    color="red",
    label="Below All Devs",
)

# Add a legend, adjust layout, and show the plot
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("plots/task5.png")
plt.show()
