import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mydata=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//diabetes.csv")
p=[]
d=[]
for i in range(len(mydata)):
	if mydata['Outcome'][i]==1:
		p.append(mydata["Pregnancies"][i])
	else:
		d.append(mydata['Pregnancies'][i])
print(len(mydata['Pregnancies']))
plt.hist(d)
plt.show()
