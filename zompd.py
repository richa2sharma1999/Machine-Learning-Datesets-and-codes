import numpy as np
import matplotlib.pyplot as plt
import json

 
data1=open("C:\\Users\\Richa Sharma\\Desktop\\pythonall\\z\\file1.json","r")
mydata1=json.loads(data1.readlines()[0])
d={}
b=0
x = []
list=[]
y = []

for i in range(len(mydata1)):
	try:
		a=mydata1[i]['restaurants']
		for i in range(len(a)):
			n=a[i]['restaurant']['name']
			city=a[i]['restaurant']['location']['city']
			if city not in list:
				x.append(city)
				list.append(city)
			g=a[i]['restaurant']['user_rating']['aggregate_rating']
			#print(g)
			if float(g)>4.0:
				print(n,city)
			
	except KeyError:
		break
#print(list)

for j in range(len(list)):
	count=0
	for i in range(len(mydata1)):
		try:
			a=mydata1[i]['restaurants']
			for i in range(len(a)):
				if(list[j]==a[i]['restaurant']['location']['city']):
					count=count+1
		except KeyError:
			break
	#print(list[j],str(count))
	d[list[j]]=count
	y.append(count)
#print(d)
#print(y)
y.sort(reverse=True)
#print(y)
final = {}
for i in d.keys():
	if(d[i] in final.keys()):
		final[d[i]].append(i)
	else:
		final[d[i]] = []
		final[d[i]].append(i)

print(final)