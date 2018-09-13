file=open("C://Users//Richa Sharma//Desktop//makemytrip//makemytrip_com-travel_sample.csv",encoding="utf-8")
f=file.readlines()[0]
import csv
import json

csvfile = open("C://Users//Richa Sharma//Desktop//makemytrip//makemytrip_com-travel_sample.csv",encoding="utf-8")
jsonfile = open("C://Users//Richa Sharma//Desktop//makemytrip//makemytrip_com-travel_sample.json","w")

fieldnames = ("area","city","country","crawl_date","highlight_value","hotel_overview","hotel_star_rating","image_urls","in_your_room","is_value_plus","latitude","longitude","mmt_holidayiq_review_count","mmt_location_rating","mmt_review_count","mmt_review_rating","mmt_review_score","mmt_traveller_type_review_count","mmt_tripadvisor_count","pageurl","property_address","property_id","property_name","property_type","qts","query_time_stamp","room_types","site_review_count","site_review_rating","sitename","state","traveller_rating","uniq_id")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    out=json.dumps([row for row in reader])
    jsonfile.write(out)

a=open("C://Users//Richa Sharma//Desktop//makemytrip//makemytrip_com-travel_sample.json","r")
print(a.readline()[]) 

