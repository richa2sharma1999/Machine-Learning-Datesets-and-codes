import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import sklearn.tree
import sklearn.ensemble

data=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//train.csv")
#print(data.head())
data=data.drop(['Cabin','Name','Ticket','PassengerId'],axis=1)
#print(data.isnull().sum())
data=data.dropna()
data=data.join(pd.get_dummies(data['Sex']))
data=data.join(pd.get_dummies(data['Embarked']))
data=data.drop(['Embarked','Sex'],axis=1)

y=data['Survived']
data=data.drop(['Survived'],axis=1)

x=data
print(x.head())
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.4)
'''clf_gini=sklearn.tree.DecisionTreeClassifier(criterion='gini',random_state=100,max_depth=3,min_samples_leaf=5)
clf=clf_gini.fit(x_train,y_train)
clf=clf_gini.fit(x_test,y_test)

print(x.head())
sklearn.tree.export_graphviz(clf,out_file='tree.dot')
print(clf_gini.score(x_train,y_train))
print(clf_gini.score(x_test,y_test))
print(x.head())'''

#randomtree

clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))
print(clf.feature_importances_)

