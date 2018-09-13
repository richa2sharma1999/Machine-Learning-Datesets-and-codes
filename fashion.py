import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import sklearn.tree
import sklearn.ensemble
import pickle
import sklearn.model_selection

data=pd.read_csv("C://Users//Richa Sharma//Desktop//fashion//fashion-mnist_train.csv")
y=data['label']
print(data.head())
data=data.drop(['label'],axis=1)
x=data
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)

#print(x_train.shape)
clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))