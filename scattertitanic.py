import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
mydata=pd.read_csv("C://Users//Richa Sharma//Desktop//pythonall//train.csv")

# Fixing random state for reproducibility
#np.random.seed(19680801)




xm=[]
ym=[]
for i in range(len(mydata)):
	if mydata["Sex"][i]=="male":
		xm.append(mydata["Fare"][i])
		ym.append(mydata["Age"][i])
#colors = "gold"
#area = (5* 5)**2  # 0 to 15 point radii
xf=[]
yf=[]
for i in range(len(mydata)):
	if mydata["Sex"][i]=="female":
		xf.append(mydata["Fare"][i])
		yf.append(mydata["Age"][i])
#colors = ["gold"]
#area = (5* 5)*2 
#sizesx=[xm,xf]
#sizesy=[ym,yf]
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(xm, ym, s=10, c='b', marker="s", label='male')
ax1.scatter(xf,yf, s=10, c='r', marker="o", label='female')
#plt.legend(loc='upper left')
plt.show()


#scatter(xm,ym,'gold');hold on;scatter(xf,yf,'blue')
#plt.scatter(xm,ym, s=area, c=colors, alpha=0.5)

