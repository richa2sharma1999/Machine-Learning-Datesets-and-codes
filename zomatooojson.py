Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import json
>>> data1=open("C:\\Users\\Richa Sharma\\Desktop\\z\\file1.json","r")
>>> mydata1=json.loads(data1.readlines()[0])
>>> d={}
>>> b=0
>>> for i in range(478):
	try:
		a=mydata1[i]['restaurants']
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

	
>>> b
52483.2
>>> d[b]
['Toit', 'Bangalore']
>>> 
