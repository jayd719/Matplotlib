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
        return CustomDataFrame  # Fix: Return class, not an instance

    def describe_extended(self):
        """Extends the describe method with additional information."""
        desc = self.describe()

        # Ensure only numeric columns are used
        numeric_df = self.select_dtypes(include=[np.number])

        if not numeric_df.empty:
            desc.loc["sum"] = numeric_df.sum()
            desc.loc["var"] = numeric_df.var()

        return desc

    def print1(self):
        print("sd")


# Example Usage
file = "pandas/data1.csv"

try:
    # Read the CSV file and pass it to CustomDataFrame
    df = CustomDataFrame(pd.read_csv(file))

    print("Extended Describe:")
    print(df.describe_extended())
    print()
    print("\nUpdated Column Names:", df.columns)
except FileNotFoundError:
    print(f"Error: The file '{file}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file}' is empty.")
except pd.errors.ParserError:
    print(f"Error: The file '{file}' could not be parsed. Check the format.")
