from twitter import *
from twitter.oauth import OAuth, read_token_file, write_token_file

oauth_token 		= "1011493451530031105-OwBPYyixDOaWWp9QSDGnMnqcfpDSXJ"
oauth_token_secret	= "QyWmHGCBzZYnHjC2l2ryn2cIVetYPKSRMQStsA3npFhMM"

consumer_key 		= "HraMa2JyRNlHelmTIBVLsUKiD"
consumer_secret 	= "MJJY7YLd3e9gxYPUEnN0bjZDrs8bbUh632KHlCYwxUo8X35p9V"

t = Twitter(auth=OAuth(oauth_token, oauth_token_secret, consumer_key, consumer_secret), secure=True, format='json')

print(t.search.tweets(q="#demonetisation",count=100))
MAX_ID = "1011529658305691648"
mydata=t.search.tweets(q="#demonetisation",count=100,max_id=MAX_ID)
import json
mydata1=json.dumps(mydata)
f=open("C://Users//Richa Sharma//Desktop//sample1.txt","w")
f.write(mydata1)
f.close()
#print(type(mydata))
#print(type(mydata1))
mydata2=open("C://Users//Richa Sharma//Desktop//sample1.txt","r")
data = mydata2.read()
data = json.loads(data)
print(len(mydata['statuses']))
#print(mydata['statuses'][2]['user']['description'][10])
word="not"
for i in range(len(data['statuses'])):
	tweet=data['statuses'][i]['user']['description']
	if(word in tweet):
		print("-->"+tweet)

