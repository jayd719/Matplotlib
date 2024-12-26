"""-------------------------------------------------------
Matplotlib: T07
-------------------------------------------------------
Author:  JD
ID:      91786
Project: DA
Version:  1.0.8
__updated__ = Thu Dec 26 2024
-------------------------------------------------------
"""

import pandas as pd
from matplotlib import pyplot as plt


# Read Data from CSV file using pandas
data = pd.read_csv("data/data3.csv")

# Set plot theme and size
plt.style.use("fivethirtyeight")
plt.figure(figsize=(12, 8))
# plot data using plt and color according to like/dislike ratio
plt.scatter(data["view_count"], data["likes"], c=data["ratio"], cmap="RdPu")
# use log for both axis
plt.xscale("log")
plt.yscale("log")

cbar = plt.colorbar()
cbar.set_label("Likes to Dislikes ratio")

plt.title("Top Trending Videos on Youtube")
plt.xlabel("Number Of veiws")
plt.ylabel("Number of likes")
plt.tight_layout()
# display plot
plt.savefig("plots/likes_to_dislike_ratio.png")
plt.show()
