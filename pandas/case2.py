import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("pandas/Salaries.csv")
print(df.head())

print(df.info())
missing_values = df.isnull().sum() / len(df) * 100
print("Missing Values in Dataset")
print(missing_values.sort_values(ascending=False))
