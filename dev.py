import os
import numpy as np
import tensorflow as tf
#import matplotlib.pyplot as plt
#import json
import pandas as pd
import sklearn
import sklearn.ensemble
import pickle
import sklearn.model_selection
#import pylab as pl
import scipy.misc as smp
from PIL import Image
#print(os.listdir('C://Users//Richa Sharma//Desktop//devanagri//DevanagariHandwrittenCharacterDataset//Train'))

folders=os.listdir('C://Users//Richa Sharma//Desktop//devanagri//DevanagariHandwrittenCharacterDataset//Train')

#print(folders)

folder=[]

list=[]

for i in range(len(folders)):
	folder=folders[i].split("_")
	if folders[i].startswith("character"):
		character=folder[2]
		list.append(character)
	if folders[i].startswith('digit'):
		digit=folder[1]
		list.append(digit)
print(list)
print(len(list))
print(folders)
print(folder)


y=[]
l=[]

#print(len(list))

for i in range(len(folders)):
	folder_content=[]
	folder_content=os.listdir('C://Users//Richa Sharma//Desktop//devanagri//DevanagariHandwrittenCharacterDataset//Train//'+str(folders[i]))
	# print(folder_content)

	for j in range(len(folder_content)):
		
		img=smp.imread('C://Users//Richa Sharma//Desktop//devanagri//DevanagariHandwrittenCharacterDataset//Train//'+str(folders[i])+"//"+str(folder_content[j]))
		img=np.array(img)
		#print(img)
		
		#img=smp.toimage(img)
		l.append(img)
		y.append(list[i])
	#print(np.array(x).shape)	

l=np.array(l)	

print(l.shape)	

y=np.array(y)	
print(y.shape)
print(y)


'''feature_columns=[]     #tensorflow

ls = [str(i) for i in range(0,1024)]'''

x = l.reshape(78200,1024)
print(x.shape)


x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)

clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))