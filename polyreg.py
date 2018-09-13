import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users//Richa Sharma//Desktop//Book1.csv")
print(data.head())
poly=sklearn.preprocessing.PolynomialFeatures(degree=3)#increasing the degree increses the accuracy.

x=data['A']
y=data['B']
x=np.array(x).reshape(-1,1)
x_poly=poly.fit_transform(x)
reg=sklearn.linear_model.LinearRegression()
print(reg.fit(x_poly,y))
print(x.shape)
print(x_poly.shape)
print(x_poly)
print(reg.score(x_poly,y))
print(reg.coef_)
print(reg.intercept_)
colors = ["blue"]
area = (5* 5)*2 
#scatter(xm,ym,'gold')
plt.scatter(x,y, s=area, c=colors, alpha=0.5)
plt.show()
plt.plot(x,reg.predict(x_poly))
plt.show()



