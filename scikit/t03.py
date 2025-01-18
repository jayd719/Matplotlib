from sklearn.datasets import fetch_california_housing
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import pandas as pd


# load boston dataset

X, y = fetch_california_housing(return_X_y=True)


print(f"X Shape: {X.shape}")
print(f"y Shape: {y.shape}")

# Split the test and train dataset
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = linear_model.LinearRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)


# plt.scatter(predictions, y_test)
# plt.show()

print(f"Model Accuracy: {model.score(X,y)}")
print(f"Regression Coffient: {model.coef_}")

print(f"Y Intercepts: {model.intercept_}")
