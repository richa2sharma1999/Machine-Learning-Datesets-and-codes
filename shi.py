import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users//Richa Sharma//Desktop//square.csv")
print(data)
x=data["A"]
x1=np.array(x)
y=data["B"]
y1=np.array(y)
print(x)
x1=x1.reshape(-1,1)
print(x1)
reg=sklearn.linear_model.LinearRegression()
reg.fit(x1,y1)
reg.predict(9)
print(reg.coef_)
print(reg.score(x1,y1))
#catter(xm,ym,'gold');hold on;scatter(x1,y1,"blue")
colors = ["blue"]
area = (5* 5)*2 
plt.scatter(x,y, s=area, c=colors, alpha=0.5)
plt.show()
plt.scatter(data["A"],data["B"])
plt.plot(data["A"],reg.predict(150))