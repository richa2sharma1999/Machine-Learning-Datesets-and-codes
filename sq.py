import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

x3d=[]
y3d=[]
z3d=[]

def fun_f(b0,b1,x):
	return b0+b1*x

def cost(b0,b1,x,y):
	n=len(x)#training_size

	c=0
	for i in range(n):
		c+=(1/n)*((y[i]-fun_f(b0,b1,x[i]))**2)
	return c

def derivative_b0(b0,b1,x,y):
	n=len(x)

	c=0
	for i in range(n):
		c+=(2/n)*(-1*(y[i]-fun_f(b0,b1,x[i])))
	return c


def derivative_b1(b0,b1,x,y):
	n=len(x)
	c=0
	for i in range(n):
		c+=(2/n)*(x[i]*((y[i]-fun_f(b0,b1,x[i]))))
	return c

def linreg(x,y,epoch):
	learning_rate=0.0005
	b0=0
	b1=0
	current_cost=cost(b0,b1,x,y)
	iter=0
	while(iter<epoch):
		b0_ =b0+learning_rate*derivative_b0(b0,b1,x,y)
		b1_ =b1+learning_rate*derivative_b1(b0,b1,x,y)

		my_cost=cost(b0_,b1_,x,y)
		x3d.append(b0)
		y3d.append(b1)
		z3d.append((b0**2+b1**2)**(1/2) )
		if(my_cost>current_cost):
			break
		else:
			current_cost=my_cost
			b0=b0_
			b1=b1_
		iter+=1
	return(b0,b1,current_cost)

#x=np.array([2,3,8,9,15,18])
#y=np.array([5,7,17,19,31,37])
x=[1,3,2,4]
y=[1,2,3,4]
b0,b1,c=linreg(x,y,100)
print(b0,b1,c)
fig = plt.figure()
ax = Axes3D(fig)

ax.plot(xs=x3d, ys=y3d, zs=z3d, zdir='z', label='ys=0, zdir=z')
plt.show()