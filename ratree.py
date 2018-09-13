import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import sklearn.tree
import sklearn.ensemble
mydata=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//Iris.csv")
#mydata.head()
#print(mydata.groupby(['Species']).mean())
#mydata=mydata.drop(['Id'],axis=1)
y=mydata['Species']
mydata=mydata.drop(['Species','Id'],axis=1)
x=mydata
#print(mydata.head())
#print(y.head())
 