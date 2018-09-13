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
import nltk
import nltk.corpus
import nltk.stem.porter

porter_stemmer=nltk.stem.porter.PorterStemmer()

stop_words=set(nltk.corpus.stopwords.words('english'))

list=[]
#for i in range(100):
	#list.append(data['comment_text'])

new_list = []

#j = 0




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
 	shabd=collections.Counter(all_words)
 	#print(shabd.keys())
 	dictionary=collections.Counter(all_words)

 	all_keys=[]
 	for i in dictionary.keys():
 		all_keys.append(i)
 	#all_keys=list(dictionary.keys())
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

 	saare_shabd=[]
 	for i in range(len(dictionary)):
 		saare_shabd.append(dictionary[i][0])

 	return all_keys
dict2={}
x=makeDictionary('C://Users//Richa Sharma//Desktop//lingspam//lingspam_public//bare//part1')
print(x)

y=[]

mail_dir='C://Users//Richa Sharma//Desktop//lingspam//lingspam_public//bare//part1'
file_paths=[os.path.join(mail_dir,f) for f in os.listdir(mail_dir)]
for file in file_paths:
	filepathTokens=file.split('\\')
	lastToken=filepathTokens[len(filepathTokens)-1]

	if lastToken.startswith('spmsg'):
		y.append(1)
	else:
		y.append(0)


vect=sklearn.feature_extraction.text.CountVectorizer()
x=vect.fit_transform(x)
print((x.shape))

print(len(y))
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)



#s = [str(i) for i in range(0,64)]
 

# = pd.DataFrame(x,columns = ls)

for i in range(len(x)):
	feature_columns.append(tf.contrib.layers.feature_column.real_valued_column(x[i]))
print(feature_columns)


estimator=tf.estimator.DNNClassifier(feature_columns=feature_columns,hidden_units=[256,128],n_classes=10)


#naive bayes algorithm
