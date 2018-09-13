import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mydata=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//diabetes.csv")
list=[]
s=[]
for i in range(len(mydata)):
	c=0
	sum=0
	if mydata['Pregnancies'][i] not in list:
		list.append(mydata['Pregnancies'][i])
		for j in range(len(mydata)):
			if mydata['Pregnancies'][i]==mydata['Pregnancies'][j]:
				sum=sum+mydata['DiabetesPedigreeFunction'][j]
				c=c+1
		print(sum/c)
		s.append(sum/c)
print(list)
print(s)
plt.plot(list,s)
plt.show()