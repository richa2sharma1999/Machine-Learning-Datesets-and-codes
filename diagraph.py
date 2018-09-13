import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import sklearn.tree
#data=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//diabetes.csv")
data=sklearn.datasets.load_diabetes()
print(data.data)
#print(data)
print(data.DESCR)
print(data.data.shape)
print(np.mean(data.data[:,0]))
x=data.data[:,0]
print(x)
y=data.target
#plt.scatter(x,y)
poly=sklearn.preprocessing.PolynomialFeatures(degree=3)#increasing the degree increses the accuracy.
x=np.array(x).reshape(-1,1)

x_poly=poly.fit_transform(x)
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x_poly,y,test_size=0.4)

reg=sklearn.linear_model.LinearRegression()
#print(reg.fit(x_poly,y))
#print(x.shape)
#print(x_poly.shape)
#x_poly=poly.fit_transform(x_train)
#reg=sklearn.linear_model.LinearRegression()
#print(x_poly)
#reg.fit(x_test,y_test)
reg.fit(x_train,y_train)

print(reg.score(x_test,y_test))
print(reg.score(x_train,y_train))


#print(reg.coef_)
#print(reg.intercept_)
plt.scatter(x,y)
plt.scatter(x,reg.predict(x_poly))
plt.show()
