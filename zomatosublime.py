import json
data1=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file1.json","r")
data2=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file2.json","r")
data3=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file3.json","r")
data4=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file4.json","r")
data5=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file5.json","r")
mydata1=json.loads(data1.readlines()[0])
mydata2=json.loads(data2.readlines()[0])
mydata3=json.loads(data3.readlines()[0])
mydata4=json.loads(data4.readlines()[0])
mydata5=json.loads(data5.readlines()[0])
b=0
d={}
z=[mydata1,mydata2,mydata3,mydata4,mydata5]
for i in range (5):
	b=0
	y=z[i]
	for i in range(len(y)):
		try:
			a=y[i]['restaurants']
			for i in range(len(a)):
				n=a[i]['restaurant']['name']
				g=a[i]['restaurant']['user_rating']['aggregate_rating']
				v=a[i]['restaurant']['user_rating']['votes']
				c=a[i]['restaurant']['location']['city']
				m=float(g)*float(v)
				d[m]=[n,c]
				if m>b:
					b=m
		except KeyError:
			break
	print(b)
	print(d[b])

