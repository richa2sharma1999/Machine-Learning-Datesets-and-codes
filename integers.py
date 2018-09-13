import pandas as pd
import sklearn
import sklearn.linear_model
import sklearn.tree
import sklearn.ensemble

data_train=pd.read_csv('C://Users//Richa Sharma//Desktop//integers//train.csv')

last_element=[]
sequence=[]
print(data_train.columns)
x_train=[]
y_train=[]
print(len(data_train['Id']))
#for i in range(len(data_train['Id'])):
for i in range(5):
	sequence=data_train['Sequence'][i]
	l=len(sequence)
	last_element=sequence[l-1]
	#del sequence[-1]
	x_train.append(sequence)
	y_train.append(last_element)

print(x_train)
print(y_train)

print(len(x_train))
print(len(data_train['Sequence'][0]))
print(data_train['Sequence'][0][178])






'''clf=sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))
print(clf.feature_importances_)'''