import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//train.csv")
print(data)
print(data.head())
print(data.columns.values)
print(data.describe())
print(data["Survived"].unique())
print(data["PassengerId"].unique())
print(data.groupby(["Cabin"]).mean())
'''xm=(data["Fare"])
ym=data["Age"]
colors = ["blue"]
area = (5* 5)*2 
#scatter(xm,ym,'gold')
plt.scatter(xm,ym, s=area, c=colors, alpha=0.5)
plt.show()
cabins=data["Cabin"].unique()
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
print(data.isnull().sum())
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
reg=sklearn.linear_model.LogisticRegression()
y=data['Survived']
data=data.drop(['Survived'],axis=1)
x=data
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
print(reg.score(x_test,y_test))
print(reg.predict(x_test))
