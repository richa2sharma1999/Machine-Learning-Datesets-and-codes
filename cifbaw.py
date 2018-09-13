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
print(dict)
x1=np.array(dict['data'])
#arr=np.array([])
for i in range(len(x1)):
	img=np.transpose(np.reshape(x1[i],(3,32,32)))
	img=Image.fromarray(img)
	img=img.convert('L')#rbg image to black
	img=np.array(img)#image converted black into array
	x=np2.append(i,img)
 
print(x.shape)

