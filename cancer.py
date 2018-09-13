import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import sklearn.tree
data=sklearn.datasets.load_breast_cancer()
print(data.DESCR)
x=data.data
y=data.target
poly=sklearn.preprocessing.PolynomialFeatures(degree=1)#increasing the degree increses the accuracy.
x_poly=poly.fit_transform(x)
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x_poly,y,test_size=0.4)
reg=sklearn.linear_model.LinearRegression()
print(x_train)
print(x_train)
x_test.shape
y_train.shape
y_test.shape
reg=sklearn.linear_model.LinearRegression()
reg.fit(x_train,y_train)
print(reg.score(x_train,y_train))
apply logisticRegression