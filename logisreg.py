import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//train.csv")
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
data=data.drop(['Survived','Age'],axis=1)
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
kfold=sklearn.model_selection.KFold(n_splits=10,random_state=7)
modelCV=sklearn.linear_model.LogisticRegression()
results=sklearn.model_selection.cross_val_score(modelCV,x,y,cv=kfold,scoring='accuracy')
print(results.mean())
#conclusions
#if we remove age, accuracy drop from approx 79% to 76%
