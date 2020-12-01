import tweepy
from credentials import *
from time import sleep

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)
api = tweepy.API(auth)

screen_name = "sinjinwest"

userId = 4281356421

targetTimeline = api.user_timeline(userId, count=1)

prompt = open('Prompt.txt', 'r')
prompt_lines = prompt.readlines()
prompt.close()

for status in targetTimeline:
	explicitContent = ["fuck", "shit", "sex", "hoe", "ass", "onlyfans", "horny", "dick", "tits", "pussy"]
	
	tweetText = status.text.lower()
	
	print(str(status.user.name + ': ' + status.text + '- Tweet ID: ' + str(status.id)))
	
	targetTweet = status.id
	
def tweet():
	for line in prompt_lines:
		try:
			if line != '\n':
				print(line)
				sleep(300)
			else:
				pass
			
		except tweepy.TweepError as e:
				print(e.reason)
			
			
	sleep(2)
		
	if any(s in tweetText for s in explicitContent):
		tweet()

