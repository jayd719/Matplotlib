import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  # for linear model
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_openml

# data = load_iris()

X, y = load_iris(return_X_y=True)


Model = LinearRegression()

Model.fit(X, y)

Model.predict(X)


Mod = KNeighborsRegressor()
Mod.fit(X, y)

pred = Mod.predict(X)

plt.scatter(pred, y)
plt.show()
