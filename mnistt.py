import sklearn
import sklearn.linear_model
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
import sklearn.tree
import sklearn.ensemble

import pylab as pl

data= sklearn.datasets.load_digits()
print(data)
print(data.images.shape)
print(data.target.shape)
pl.matshow(data.images[0])
#pl.show()
print(data.target)
x=data.images.reshape(1797,64)
print(x.shape)
y=data.target
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)

print(x_train.shape)

clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))
#print(clf.feature_importances_)


