import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
mydata=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//train.csv")
#print(mydata["Sex"][0])
m=0
f=0
for i in range(len(mydata)):
	if mydata["Sex"][i]=="male":
		m=m+1
	else:
		f=f+1
print(m,f)
labels = 'Male', 'Female'
sizes = [m,f]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()