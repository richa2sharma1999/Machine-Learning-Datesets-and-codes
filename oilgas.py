import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//oilgas.csv")
#print(data)
#print(data.head())
#print(data.columns.values)
#print(data.describe())
#print(data["Survived"].unique())
#print(data["PassengerId"].unique())
#print(data.groupby(["Cabin"]).mean())
'''xm=(data["Fare"])
ym=data["Age"]
colors = ["blue"]
area = (5* 5)*2 
#scatter(xm,ym,'gold')
plt.scatter(xm,ym, s=area, c=colors, alpha=0.5)
plt.show()'''
'''cabins=data["Cabin"].unique()
survival={}

i = 0
for s in data["Survival"]:
	cabin = data["Cabin"][i]
	if  cabin not in survival.keys():
		survival[cabin] = 0
	survival[cabin]+=s
	i += 1

plt.plot(survival.keys(),survival.values())
plt.show()'''
'''print(data.isnull().sum())
data=data.drop(['Cabin','PassengerId','Name','Ticket','Fare'],axis=1)
print(data)
print(data.isnull().sum())
data=data.join(pd.get_dummies(data['Sex']))
print(data)
data=data.drop(['Sex'],axis=1)
print(data)
print(data.groupby(['Embarked']).mean())
data=data.join(pd.get_dummies(data['Embarked']))
data=data.drop(['Embarked'],axis=1)
data=data.dropna()
print(data)
reg=sklearn.linear_model.LogisticRegression()'''
'''y=data['Survived']
print(x.shape)
y.shape
reg.fit(x,y)
print(reg.score(x,y))
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.4)
#print(x)
#print(y)
reg=sklearn.linear_model.LogisticRegression()
x_test.shape
y_train.shape
y_test.shape
reg=sklearn.linear_model.LogisticRegression()
reg.fit(x_train,y_train)
print(reg.score(x_train,y_train))
print(reg.score(x_test,y_test))'''
x=data['year']
y=data['oil_price_nom']
colors = ["blue"]
area = (5* 5)*2 
#scatter(xm,ym,'gold')
plt.scatter(x,y, s=area, c=colors, alpha=0.5)
plt.show()

poly=sklearn.preprocessing.PolynomialFeatures(degree=4)#increasing the degree increses the accuracy.
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
#plt.show()
plt.plot(x,reg.predict(x_poly))
plt.show()