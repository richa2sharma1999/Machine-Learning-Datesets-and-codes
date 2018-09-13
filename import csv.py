import csv
with open("C://Users//Richa Sharma//Desktop//makemytrip//makemytrip_com-travel_sample.csv",encoding='utf-8') as csvfile:
	read=csv.reader(csvfile,delimiter=',',quotechar='"')
	for row in read:
	 print(row)