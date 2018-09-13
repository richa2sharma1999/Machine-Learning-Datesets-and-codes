import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import sklearn.tree
mydata=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//Iris.csv")
mydata.head()
print(mydata.groupby(['Species']).mean())

mydata=mydata.drop(['Id'],axis=1)
y=mydata['Species']
mydata=mydata.drop(['Species'],axis=1)
x=mydata
#print(mydata.head())
#print(y.head())
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)
clf_gini=sklearn.tree.DecisionTreeClassifier(criterion='gini',random_state=100,max_depth=3,min_samples_leaf=5)
clf=clf_gini.fit(x_train,y_train)
print(x.head())
sklearn.tree.export_graphviz(clf,out_file='tree.dot')
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))
print(x.shape)

