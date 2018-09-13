import sklearn

import sklearn.datasets

import sklearn.ensemble

import pandas as pd

import numpy as np

import sklearn.linear_model

import sklearn.model_selection

import pickle

import pylab as pl

import scipy.misc as smp

from PIL import Image

 

with open("D://mchine learning bvp//ina_singhal//train","rb") as fo:

                dict=pickle.load(fo,encoding='latin1')

#print(dict)

 

print(dict["data"].shape)

#pl.matshow(dict["data"])

#pl.show()

x=np.array(dict["data"])

#img=np.transpose(np.reshape(x[0],(3,32,32)))

#img=smp.toimage(img)

#img.show()

with open("D://mchine learning bvp//ina_singhal//meta","rb") as fo:

                meta=pickle.load(fo)

y=dict["coarse_labels"]

x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)

clf=sklearn.ensemble.RandomForestClassifier(random_state=0) 

clf.fit(x_train,y_train)

#print(clf.score(x_test,y_test))

 

"""for i in range(len(x)):

                img=np.transpose(np.reshape(x[i],(3,32,32)))

                img=smp.toimage(img)

                #img.show()

                col = Image.open("C://Users//Ina//Desktop//photo.jpg")

                gray = col.convert('L')

                bw = gray.point(lambda x: 0 if x<128 else 255, '1')

                bw.save("C://Users//Ina//Desktop//out.jpg")

"""

l=list()

for i in range(len(x)):

                img=np.transpose(np.reshape(x[i],(3,32,32)))

                img=smp.toimage(img)

 

                img=img.convert('L')

                img=np.array(img)

                l.append(img)

 

ar=np.array(l)

ar=ar.reshape(50000,-1)

print(ar.shape)

x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(ar,y,test_size=0.2)

clf=sklearn.ensemble.RandomForestClassifier(random_state=0) 

clf.fit(x_train,y_train)

print(clf.score(x_test,y_test))