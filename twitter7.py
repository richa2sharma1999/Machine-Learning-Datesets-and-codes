from twitter import*
from twitter.oauth import OAuth,read_token_file,write_token_file
oauth_token 		= "	1011493451530031105-OwBPYyixDOaWWp9QSDGnMnqcfpDSXJ"
oauth_token_secret	= "	QyWmHGCBzZYnHjC2l2ryn2cIVetYPKSRMQStsA3npFhMM"

consumer_key 		= "	HraMa2JyRNlHelmTIBVLsUKiD"
consumer_secret 	= "	MJJY7YLd3e9gxYPUEnN0bjZDrs8bbUh632KHlCYwxUo8X35p9V"

t = Twitter(auth=OAuth(oauth_token, oauth_token_secret, consumer_key, consumer_secret), secure=True, format='json')


print(t.search.tweets(q="#demonetisation",count=100))

#MAX_ID = "GET YOUR MAX_ID in the first response you get"
#t.search.tweets(q="#demonetisation",count=100,max_id=MAX_ID)
