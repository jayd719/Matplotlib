import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


dataset = pd.read_csv("diabetes.csv")
print(len(dataset))
print(dataset.head())


# replace zeros
zero_not_allowd = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for col in zero_not_allowd:
    dataset[col] = dataset[col].replace(0, np.nan)
    mean = int(dataset[col].mean(skipna=True))
    dataset[col] = dataset[col].replace(np.nan, mean)


print(dataset.head())

X = dataset.iloc[:, 0:-1]
y = dataset.iloc[:, -1]

# feature scaling
ss = StandardScaler()
X = ss.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

n = int(math.sqrt(len(y_test)))
n = n - 1 if n % 2 == 0 else n
print(n)

classifier = KNeighborsClassifier(n_neighbors=n, p=2, metric="euclidean")


classifier.fit(x_train, y_train)
print("Trained Successfully")
y_pred = classifier.predict(x_test)

# evalute the model
cm = confusion_matrix(y_test, y_pred)
print(cm)

f1score = f1_score(y_test, y_pred)
print(f1score)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
