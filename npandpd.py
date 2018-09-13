import numpy as np
import pandas as pd
print(np.empty([1,2]))
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print (x)
print (x.shape)
print (np.empty_like(x))
print (np.identity(2))
print (np.identity(2,dtype="int"))
print (np.ones([3,3]))
print (np.linspace(0,100,100))
print (np.linspace(0,100,100,dtype="int"))
print (np.linspace(0,100,50,dtype="int"))
print (np.sin(np.linspace(0,100,100,dtype="int")))
print (np.diag(x))


statename="Bihar"
mydata=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//lecture9.csv")
print(mydata['State'][7])


u=np.array(mydata.loc[:,["State","Professor and Equivalent - Total"]])
#print(u)
print (mydata["Professor and Equivalent - Total"][5])
#print (mydata.loc[2:2,["State"]])
for i in range(len(u)):
	if u[i][0]==statename:
		print(u[i][1])
		break


