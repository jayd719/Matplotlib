import pandas as pd
import numpy as np

df = pd.read_csv("pandas/data1.csv")

print("\n\nTop 10 Rows fo data set")
print(df.head(10))

print("\n\nLast 10 Rows of dataset")
print(df.tail(10))


print("\n\nDataset Informations")
print(df.info())

print("\n\nMissing values")
print(df.isnull().sum())


print(f"\n\nNumber of rows:{df.shape[0]}")
print(f"Number of cols:{df.shape[1]}")

print("\ncols")
print(df.columns)
print("Number of cols:", len(df.columns))
print("Number of row", len(df))


print(f'highest purchasing price: {df["Purchase Price"].max()}')
print(f'Lowest purchasing price: {df["Purchase Price"].min()}')
print(f'Average Sales Price: {df["Purchase Price"].mean():.2f}')


print(f"Number of people with FRENCH as language: {(df['Language']=='fr').count()}")
