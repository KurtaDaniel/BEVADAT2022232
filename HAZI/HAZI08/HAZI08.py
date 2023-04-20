# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error

# %%
'''
Készíts egy függvényt, betölti majd vissza adja az iris adathalmazt.


Egy példa a kimenetre: iris
return type: sklearn.utils.Bunch
függvény neve: load_iris_data
'''

# %%
def load_iris_data():
    return load_iris()

#ir = load_iris_data()
#ir['target']
#ir['data']


# %%
'''
Készíts egy függvényt, ami a betölti az virágokhoz tartozó levél méretket egy dataframebe, majd az első 5 sort visszaadja.
Minden oszlop tartalmazza, hogy az milyen mérethez tartozik.

Egy példa a bemenetre: iris
Egy példa a kimenetre: iris_df
return type: pandas.core.frame.DataFrame
függvény neve: check_data
'''

# %%
def check_data(iris):
    return pd.DataFrame(iris.data, columns=iris.feature_names).head(5)

#print(check_data(load_iris_data()))

# %%
''' 
Készíts egy függvényt ami előkészíti az adatokat egy lineaáris regressziós model feltanításához.
Featurejeink legyenek a levél méretek kivéve a "sepal length (cm)", ez legyen a targetünk.

Egy példa a bemenetre: iris
Egy példa a kimenetre: X, y
return type: (numpy.ndarray, numpy.ndarray)
függvény neve: linear_train_data
'''

# %%
def linear_train_data(iris):
    iris = pd.DataFrame(iris.data, columns=iris.feature_names)
    X = iris[['sepal width (cm)','petal length (cm)','petal width (cm)']].values
    y = iris['sepal length (cm)'].values
    return X, y  

#b = load_iris_data()
#c = pd.DataFrame(b.data, columns=b.feature_names)
#X, y = linear_train_data(b)     

# %%
''' 
Készíts egy függvényt ami előkészíti az adatokat egy logisztikus regressziós model feltanításához.
Featurejeink legyenek a levél méretek, targetünk pedig a 0, 1-es virág osztályok.
Fontos csak azokkal az adatokkal tanítsunk amihez tartozik adott target. 

Egy példa a bemenetre: iris
Egy példa a kimenetre: X, y
return type: (numpy.ndarray, numpy.ndarray)
függvény neve: logistic_train_data
'''

# %%
def logistic_train_data(iris):
    y = iris['target']
    iris = pd.DataFrame(iris.data, columns=iris.feature_names)
    X = iris[['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']].values
    return X, y

#b = load_iris_data()
#c = pd.DataFrame(b.data, columns=b.feature_names)
#logistic_train_data(b)  

# %%
'''
Készíts egy függvényt ami feldarabolja az adatainkat train és test részre. Az adatok 20%-át használjuk fel a teszteléshez.
Tegyük determenisztikussá a darabolást, ennek értéke legyen 42.

Egy példa a bemenetre: X, y
Egy példa a kimenetre: X_train, X_test, y_train, y_test
return type: (numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray)
függvény neve: split_data
'''

# %%
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test



#X_train, X_test, y_train, y_test = split_data(X,y)

# %%
'''
Készíts egy függvényt ami feltanít egy lineaáris regressziós modelt, majd visszatér vele.

Egy példa a bemenetre: X_train, y_train
Egy példa a kimenetre: model
return type: sklearn.linear_model._base.LinearRegression
függvény neve: train_linear_regression
'''

# %%
def train_linear_regression(X_train, y_train):
    m = 0
    c = 0

    L = 0.0001  # The learning Rate
    epochs = 1000  # The number of iterations to perform gradient descent

    n = float(len(X_train)) # Number of elements in X

    # Performing Gradient Descent 
    #losses = []
    for i in range(epochs): 
        y_pred = m*X_train + c  # The current predicted value of Y

        residuals = y_train - y_pred
        #loss = np.sum(residuals ** 2)
        #losses.append(loss)
        D_m = (-2/n) * sum(X_train * residuals)  # Derivative wrt m
        D_c = (-2/n) * sum(residuals)  # Derivative wrt c
        m = m - L * D_m  # Update m
        c = c - L * D_c  # Update c

    return m*X_train + c

#print(train_linear_regression(X_train,y_train))
#m*X_train + c

# %%
'''
Készíts egy függvényt ami feltanít egy logisztikus regressziós modelt, majd visszatér vele.

Egy példa a bemenetre: X_train, y_train
Egy példa a kimenetre: model
return type: sklearn.linear_model._base.LogisticRegression
függvény neve: train_logistic_regression
'''

# %%


# %%
''' 
Készíts egy függvényt, ami a feltanított modellel predikciót tud végre hajtani.

Egy példa a bemenetre: model, X_test
Egy példa a kimenetre: y_pred
return type: numpy.ndarray
függvény neve: predict
'''

# %%
def predict(model, X_test):
    pred = []
    for X in X_test:
        y_pred = model
        pred.append(y_pred)
    return y_pred


# %%
'''
Készíts egy függvényt, ami vizualizálni tudja a label és a predikciók közötti eltérést.
Használj scatter plotot a diagram elkészítéséhez.

Diagram címe legyen: 'Actual vs Predicted Target Values'
Az x tengely címe legyen: 'Actual'
Az y tengely címe legyen: 'Predicted'

Egy példa a bemenetre: y_test, y_pred
Egy példa a kimenetre: scatter plot
return type: matplotlib.figure.Figure
függvény neve: plot_actual_vs_predicted
'''

# %%


# %%
''' 
Készíts egy függvényt, ami a Négyzetes hiba (MSE) értékét számolja ki a predikciók és a valós értékek között.

Egy példa a bemenetre: y_test, y_pred
Egy példa a kimenetre: mse
return type: float
függvény neve: evaluate_model
'''

# %%


