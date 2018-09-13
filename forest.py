import pandas as pd
import sklearn
import sklearn.linear_model
import sklearn.tree
import tensorflow as tf
import sklearn.ensemble
import matplotlib.pyplot as plt


data=pd.read_csv('C://Users//Richa Sharma//Desktop//forest//train.csv')

y=data['Cover_Type']
data=data.drop(['Cover_Type','Id','Soil_Type7'],axis=1)
x=data


x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)




clf_gini = sklearn.tree.DecisionTreeClassifier(criterion='gini',random_state=100,max_depth=14,min_samples_leaf=5)
clf_gini.fit(x_train,y_train)
print("Using Decision Tree:"+str(clf_gini.score(x_test,y_test)))

clf = sklearn.ensemble.RandomForestClassifier(random_state=0)
clf.fit(x_train,y_train)
print('Using Random Forest:'+str(clf.score(x_test,y_test)))

reg = sklearn.linear_model.LogisticRegression()
reg.fit(x_train,y_train)
print("Using Logistic Regression:"+str(reg.score(x_test,y_test)))

model = sklearn.svm.SVC()
model.fit(x_train,y_train)
print("Using Support Vector Machine:"+str(model.score(x_test,y_test)))

reg = sklearn.linear_model.LinearRegression()
reg.fit(x_train,y_train)
print("Using LinearRegression:"+str(reg.score(x_test,y_test)))












'''labels = 'DecisionTree', 'RandomForest', 'LogisticRegression', 'SVM','LinearRegression'
sizes = [0.5889550264550265, 0.8349867724867724,0.6676587301587301 , 0.13326719576719576,0.3980040987896637]
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.2, 0, 0,0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()'''