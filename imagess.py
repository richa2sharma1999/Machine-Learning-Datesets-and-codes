import numpy as np
import pandas as pd
import sklearn
import sklearn.linear_model
import sklearn.tree
import sklearn.ensemble
import scipy.misc as smp
import matplotlib.pyplot as plt
import tensorflow as tf

data=pd.read_csv('C://Users//Richa Sharma//Desktop//face//training.csv')
#print(len(data.columns))
#print(data["Image"][0])
#c=np.array([])
ls=[]
for i in range(10):
	c=data['Image'][i].split(" ")
	ls.append(c)
#print(c)
#print(len(ls))
x=ls

mydata=np.array([c])
print(mydata.shape)
mydata=mydata.reshape(96,96)
mydata=np.array(mydata,np.float32)

#print(data[])
#print(mydata.shape)
plt.imshow(mydata,cmap="gray")

#plt.imshow()
#matplotlib.pyplot.matshow(mydata)

#mydata=np.array(mydata,np.float32)
#img = smp.toimage(mydata)       # Create a PIL image

l=[]
for i in range(30):
	l.append(data.columns[i])
print(l)
xm=[]
ym=[]

'''for i in range(len(l)):
	if i%2==0:
		xm.append(data[l[i]][4])
	else:
		ym.append(data[l[i]][0])'''
#print(xm)
#print(ym)

#img = smp.toimage(mydata)  



'''arr=np.array(xm)
print(arr.shape)
arr=arr.reshape(1,15)
mydata=np.array(arr,np.float32)
imgx = smp.toimage(arr) 
plt.scatter(xm,ym)
plt.show()'''
y=[]
for i in range(10):
	label=[]
	for j in range(len(l)):
		label.append(data[l[j]][i])
	y.append(label)
#print(len(label))
feature_columns=[]
for key in data.keys():
	if key=='Image':
		feature_columns.append(tf.contrib.layers.feature_column.real_valued_column(key))
print(feature_columns)

estimator=tf.estimator.DNNClassifier(feature_columns=feature_columns,hidden_units=[10],n_classes=30)

x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)

def my_input_fn():
	#y=y_train
	#x=dict(x_train) 
	return dict(x_train),y_train

estimator.train(input_fn=my_input_fn,steps=200)

def my_input_fn2():
	y=y_test
	x=dict(x_test)
	return x,y
print(estimator.evaluate(input_fn=my_input_fn2,steps=1))


