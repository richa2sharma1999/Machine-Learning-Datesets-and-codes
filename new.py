import json
a=open("C://Users//Richa Sharma//Desktop//makemytrip//makemytrip_com-travel_sample.json","r")
b=json.loads(a.readline())
z=0
d={}
def insertOrReject(value,list):
	if(len(list)<5):
		list.append(value)
	else:
		if value not in list:
			list.append(value)
		list.sort()
		del list[0]
	return list
j=[]
city_list=[]
u={}
for i in range(len(b)):
	f=b[i]
	c=f['mmt_tripadvisor_count']
	n=f['property_name']
	y=f['mmt_review_score']
	s=f['city']
	if s not in city_list:
		city_list.append(s)
	try:
		z=float(c)*float(y)
		d[z]=[n,z,s]
		insertOrReject(z,j)
	except ValueError:
		continue
obj = [[] for i in range(len(city_list))]
for i in range(len(city_list)):
	u[city_list[i]]=obj[i]
for i in range(len(b)):
	f=b[i]
	c=f['mmt_tripadvisor_count']
	n=f['property_name']
	y=f['mmt_review_score']
	s=f['city']
	try:
		z=float(c)*float(y)
		u[s].append(z)
		d[z]=[n,z,s]
		insertOrReject(z,j)
	except ValueError:
		continue
print(j)
for i in range (5):
	print(d[j[i]])
print(len(u['Udaipur']))


