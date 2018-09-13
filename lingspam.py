import sklearn
import sklearn.linear_model
import sklearn.datasets
import sklearn.naive_bayes
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.tree
import sklearn.ensemble
import pickle
import sklearn.model_selection
import pylab as pl
import scipy.misc as smp
from PIL import Image

import numpy as np
import sklearn.feature_extraction.text
import os
import collections
def makeDictionary(root_dir):
 	all_words=[] 
 	emails=[os.path.join(root_dir,f) for f in os.listdir(root_dir)]
 	print(len(emails))

 	for mail in emails:
 		with open(mail) as m:
 			for line in m:
 				words=line.split()
 				all_words +=words
 	print(len(all_words))
 	dictionary=collections.Counter(all_words)
 	all_keys=list(dictionary.keys())
 	times_removed=0
 	for item in all_keys:
 		if item.isalpha()==False:
 			del dictionary[item]
 			times_removed +=1
 		elif len(item)==1:
 			times_removed +=1
 			del dictionary[item]
 	print(len(all_keys))
 	print(times_removed)

 	dictionary=dictionary.most_common(300)

 	return dictionary
d=makeDictionary('C://Users//Richa Sharma//Desktop//lingspam//lingspam_public//bare//part1')
#print(d)
#print(len(var.keys())
def extract_features(mail_dir):
	file_paths=[os.path.join(mail_dir,f) for f in os.listdir(mail_dir)]
	features_matrix=np.zeros((len(file_paths),300))
	train_labels=np.zeros(len(file_paths))
	print(features_matrix.shape)
	count=0
	doctID=0
	for file in file_paths:
		with open(file) as fi:
			for i,line in enumerate(fi):
				if i==2:
					words=line.split()
					print(line)
					for word in words:
						wordID=0
						for i,t in enumerate(d):
							if t[0]==word:
								wordID=i 
								features_matrix[doctID,wordID]=words.count(word)
		train_labels[doctID]=0
		filepathTokens=file.split('\\')
		lastToken=filepathTokens[len(filepathTokens)-1]

		if lastToken.startswith('spmsg'):
			train_labels[doctID]=1
			count=count+1
		doctID=doctID+1
	return features_matrix,train_labels

x,y=extract_features('C://Users//Richa Sharma//Desktop//lingspam//lingspam_public//bare//part1')
print(x)
print(y)
print(len(y))
print(x.shape)


x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)

#naive bayes algorithm
model=sklearn.naive_bayes.GaussianNB()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))

#random forest algorithm
'''clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))'''

#logistic regresssion algrithm
'''reg=sklearn.linear_model.LogisticRegression()
reg.fit(x_train,y_train)
print(reg.score(x_test,y_test))'''

#decision tree algorithm
#toxic comment classification kaggle
x_train=['today is 10th july 2018','our current location is delhi']
vect=sklearn.feature_extraction.text.CountVectorizer()
tf_train=vect.fit_transform(x_train)
