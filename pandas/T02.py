import pandas as pd

dict1 = {
    "Name": ["Priyang", "Aadhya", "Krisha", "Vedant", "Parshv", "Mittal", "Archana"],
    "Marks": [98, 89, 99, 87, 90, 83, 99],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female", "Female"],
}
df1 = pd.DataFrame(dict1)
print(df1)


# Display top three rows of dataframe
print("\nTop Three Rows")
print(df1.head(3))  # first 5 by default

print("\nLast Three Row")
print(df1.tail(3))  # last five by default

print("\nShape of dataset")
print(df1.shape)
print(f"Number of Rows: {df1.shape[0]}")
print(f"Number of Cols: {df1.shape[1]}")

print("\nInformation About Dataset")
print(df1.info())

print("\Check Null Values in dataset")
print(df1.isnull().sum(axis=0))

print("\nGet Overall Stats about dataset")
print(df1.describe(include="all"))  # display stats about numeric cols only by default
print(f"Median {df1['Marks'].median():.2f}")


print("Unquie Value")
print(df1["Gender"].unique())
print(df1["Gender"].nunique())

print("\nValues Counts")
values = df1["Gender"].value_counts()
print(type(values))
print(values)
print(values.index)
print(type(values.index))

print("conditions")
print(df1[(df1["Marks"] >= 90) & (df1["Marks"] <= 100)])

print("between Method")
print(df1["Marks"].between(90, 100).sum())


def marks(mark):
    return mark // 2


df1["half"] = df1["Marks"].apply(marks)
df1["double"] = df1["Marks"].apply(lambda x: x**2)
print(df1)
print("\n\n")

print(df1["Name"].apply(len))


# map functions
print("map Function")
df1["gender_updated"] = df1["Gender"].map({"Male": 1, "Female": 0})
print(df1)

print("drop cols")
df1.drop(["double"], axis=1, inplace=True)
print(df1)

df1.sort_values(by=["Marks", "Name"], inplace=True)
print(df1)
