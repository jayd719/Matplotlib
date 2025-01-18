from sklearn.datasets import fetch_openml
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import math


df = pd.read_csv("titanic.csv")
print("\nInformation About The Dataset::")
print(df.info())
print("\nNull Values in the dataset::")
print(df.isnull())
print("\nTotal Null Values::")
print(df.isnull().sum())

sns.set_theme("paper")
miss_value_percentage = pd.DataFrame(
    round(df.isnull().sum() / len(df) * 100, 2), columns=["Percentage"]
)
print(miss_value_percentage)

miss_value_percentage.plot(
    kind="bar", title="Missing Values In The Dataset", ylabel="percentage"
)

# plt.show()


print(f"size of the dataset: {df.shape}")
df.drop(["Cabin"], axis=1, inplace=True)  # dropping the entire column
print(f"Size of data after dropping featuter: {df.shape}")


# Value Imputation
# Simple Imputer: it replaces all missing values with a statistically calculated  from the other values in column. using statitics: mean, mode, median, most frequenct and constant
# Replance Null Valuse

from sklearn.impute import SimpleImputer

print(f"Number of null values before imputing: {df.Age.isnull().sum()}")

# Simple Imputer arguments:
# missing values
# stargery
# fill value if replacing with constant value

imp = SimpleImputer(strategy="mean")
df["Age"] = imp.fit_transform(df[["Age"]])
print(f"Number of Null Values After Imputation: {df.Age.isnull().sum()}")

# ^^ this cannot be achived on string data.


def get_parameters(df):
    parameters = {}
    for col in df.columns[df.isnull().any()]:
        print(col)
        if df[col].dtype in ["float64", "int64", "int32"]:
            strategy = "mean"
        else:
            strategy = "most_frequent"
        missing_values = df[col][df[col].isnull()].values[0]
        parameters[col] = {"missing_values": missing_values, "strategy": strategy}
    return parameters


parameters = get_parameters(df)
print(parameters)


for col, parm in parameters.items():
    miss_values = parm["missing_values"]
    strategy = parm["strategy"]

    imp = SimpleImputer(missing_values=miss_values, strategy=strategy)
    # df[col] = imp.fit_transform(df[[col]])


print(df.isnull().sum())

# Feature Engineering is the process of transforming raw data into meaningful features that improve the performance of Machine Learning models. It involves creating, selecting, or modifying features from existing data to enhance predictive power.

df["Family"] = df["SibSp"] + df["Parch"]
df.loc[df["Family"] > 0, "Travelled_Alone"] = 0
df.loc[df["Family"] == 0, "Travelled_Alone"] = 1
df["Travelled_Alone"].value_counts().plot(title="Passanger Travelled ALong", kind="bar")
# plt.show()


# Data Encoding
from sklearn.preprocessing import OneHotEncoder

df["Sex"] = OneHotEncoder().fit_transform(df[["Sex"]]).toarray()[:, 1]
print(df.head())


# Data Scalling
# if data in any condition has points far from each other, scaling is a techquine to make them closer to each other.
# to reduce the effect of scale on learing alogrithm


# Data Normalization
# MinMaxScalar
# standardScalar


from sklearn.preprocessing import StandardScaler

# only scale  numerical columns
num_cols = df.select_dtypes(include=["int64", "float64", "int32"]).columns
print(num_cols)


ss = StandardScaler()

df[num_cols] = ss.fit_transform(df[num_cols])
print(df[num_cols].describe())


from sklearn.preprocessing import MinMaxScaler

minmax = MinMaxScaler()
df[num_cols] = minmax.fit_transform(df[num_cols])
print(df[num_cols].describe())
