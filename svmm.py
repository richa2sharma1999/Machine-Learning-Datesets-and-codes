import sklearn
import sklearn.svm
import sklearn.model_selection
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import sklearn.tree
import matplotlib.pyplot as plt


#iris data-set
'''df=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//Iris.csv")
df=df.drop(['Id'],axis=1)
y=df['Species']
df=df.drop(['Species'],axis=1)
x=df'''

#digits/mnist dataset
'''
data= sklearn.datasets.load_digits()
x=data.images.reshape(1797,64)
#print(x.shape)
y=data.target'''

#cifar dataset
import pickle
with open("C://Users//Richa Sharma//Desktop//cifar//cifar-100-python//train",'rb') as fo:
	dict=pickle.load(fo,encoding='latin1')
print(dict['data'].shape)
x=np.array(dict['data'])
y=dict["coarse_labels"]

x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)

model=sklearn.svm.SVC()                             
model.fit(x_train,y_train)
print(model.score(x_test,y_test))

