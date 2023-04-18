from LinearRegressionSkeleton import LinearRegression
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from matplotlib import pyplot as plt
a = LinearRegression(epochs=5000)
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
X = df['petal width (cm)'].values
y = df['sepal length (cm)'].values
#X = df['petal length (cm)'].values
#y = df['petal width (cm)'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

a.fit(X_train,y_train)
a.predict(X_test)
a.test(X_test,y_test)