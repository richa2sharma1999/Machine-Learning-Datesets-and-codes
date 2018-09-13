Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import json
>>> for i in range (5):
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
