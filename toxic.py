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
import nltk
import nltk.corpus
import nltk.stem.porter

porter_stemmer=nltk.stem.porter.PorterStemmer()

import numpy as np
import sklearn.feature_extraction.text
import os
import collections

'''x_train=['today is 10th july 2018', 
		 'our current location is delhi']
vect=sklearn.feature_extraction.text.CountVectorizer()
tf_train=vect.fit_transform(x_train)
print()'''

data=pd.read_csv("C://Users//Richa Sharma//Desktop//toxicom//train.csv")
# print(data.head())
# print(data['comment_text'].head())
stop_words=set(nltk.corpus.stopwords.words('english'))
list=[]
#for i in range(100):
	#list.append(data['comment_text'])

new_list = []

#j = 0


for sentence in data['comment_text'][:1000]:
	sentence = sentence.lower()
	words=sentence.split(" ")
	final_sentence=[]
	new_sentence=""
	for word in words:
		#print(word)
		if word not in stop_words:
			#print(word)
			word_stem=porter_stemmer.stem(word)
			final_sentence.append(word_stem)
	new_sentence = (" ".join(final_sentence))
	new_list.append(new_sentence)
#	j += 1
print(len(new_list))
all_words=[] 

for line in new_list:
 	words=line.split()
 	all_words +=words
 	
print(len(all_words))
 	
dictionary=collections.Counter(all_words)


l = []

for i in dictionary.keys():
		l.append(i)


#all_keys=list(dictionary.keys())
times_removed=0
for item in l:
 	if item.isalpha()==False:
 		del dictionary[item]
 		times_removed +=1
 	elif len(item)==1:
 		times_removed +=1
 		del dictionary[item]
print(len(l))
print(times_removed)
dictionary=dictionary.most_common(300)

'''x=new_list
#for i in range(len(data)):
#	x.append(data["comment_text"][i])

y=data["toxic"][:1000]

vect=sklearn.feature_extraction.text.CountVectorizer()
tf=vect.fit_transform(new_list)
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(tf,y,test_size=0.2)

#naive bayes algorithm
model=sklearn.linear_model.LogisticRegression()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))'''