import os
import pandas as pd
import numpy as np
from datetime import datetime

# os.system("clear")
print()
print(datetime.today())


class CustomDataFrame(pd.DataFrame):
    """A custom DataFrame with additional functionalities."""

    @property
    def _constructor(self):
        return CustomDataFrame

    def save(self, filename="data.json"):
        self.to_json(filename, orient="records")


file = "data.json"
try:
    # Read the CSV file and pass it to CustomDataFrame
    df = CustomDataFrame(pd.read_json(file))
    print(df)

except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")
