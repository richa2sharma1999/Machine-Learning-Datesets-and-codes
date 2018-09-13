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
import pylab as pl
import scipy.misc as smp
from PIL import Image
with open("C://Users//Richa Sharma//Desktop//cifar//cifar-100-python//train",'rb') as fo:
	dict=pickle.load(fo,encoding='latin1')
print(dict['data'].shape)
x=np.array(dict['data'])

img=np.transpose(np.reshape(x[0],(3,32,32)))
img=Image.fromarray(img)
#pl.matshow(img)
img.show()

'''with open("C://Users//Richa Sharma//Desktop//cifar//cifar-100-python//meta",'rb') as fo:
	meta=pickle.load(fo,encoding='latin1')

#print(meta)

y=dict["coarse_labels"]
#print(y)
#print(meta)
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)

#print(x_train.shape)
clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))'''