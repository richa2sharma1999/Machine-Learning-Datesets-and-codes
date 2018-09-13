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
for i in range(len(b)):
	f=b[i]
	c=f['mmt_tripadvisor_count']
	n=f['property_name']
	y=f['mmt_review_score']
	try:
		z=float(c)*float(y)
		d[z]=[n]
		insertOrReject(z,j)
	except ValueError:
		continue
print(j)
d[21508.8]="abcd"
for i in range (5):
	print(d[j[i]])