import sklearn
import sklearn.linear_model
import sklearn.datasets
boston = sklearn.datasets.load_boston()
#feature names
#boston.feature_names
#for real data
#boston.data
#print(boston)
x=boston.data
y=boston.target
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.4)
print(x)
print(y)
reg=sklearn.linear_model.LinearRegression()
'''reg.fit(x,y)
print(reg.score(x,y))
print(x_train.shape)'''
x_test.shape
y_train.shape
y_test.shape
reg=sklearn.linear_model.LinearRegression()
reg.fit(x_train,y_train)
print(reg.score(x_train,y_train))