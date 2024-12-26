import os
import csv
from collections import Counter
from matplotlib import pyplot as plt

# Create output directory for plots
os.makedirs("./plots/", exist_ok=True)

# Read the CSV file and count programming languages
with open("data/data.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    language_counter = Counter()
    for row in csv_reader:
        # Split the languages in the "LanguagesWorkedWith" column and update the counter
        languages = row["LanguagesWorkedWith"].split(";")
        language_counter.update(languages)

# Configure the plot style and size
plt.style.use("fivethirtyeight")
plt.figure(figsize=(15, 8))

# Create Pie Chart
languages, counts = zip(*reversed(language_counter.most_common(15)))
plt.pie(
    counts,
    labels=languages,
    wedgeprops={"edgecolor": "k"},
)


# Title and Labels
plt.title("Most Used Programming Languages")

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("plots/most_used_languages_pie.png")

# Display the plot
plt.show()
