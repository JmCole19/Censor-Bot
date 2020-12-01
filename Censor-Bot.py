import tweepy
from credentials import *
from time import sleep
import schedule

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(akey, asecret)
api = tweepy.API(auth)

userId = 4281356421

targetTimeline = api.user_timeline(userId, count=25)

prompt = open('Prompt.txt', 'r')
prompt_lines = prompt.readlines()
prompt.close()

for status in targetTimeline:
	explicitContent = ["fuck", "shit", "sex", "hoe", "ass", "onlyfans", "horny", "dick", "tits", "pussy", "nude", "nudes"]
	tweetText = status.text.lower()	
	targetTweet = status.id

	print(str(status.user.name + ': ' + status.text + ' - Tweet ID: ' + str(status.id)))
		
def tweet():
	for line in prompt_lines:
		try:
			if any(s in tweetText for s in explicitContent):
				api.update_status(str("Hello @" + status.user.screen_name + ',' + line), targetTweet)
				sleep(3)
			else:
				pass
			
		except tweepy.TweepError as e:
				print(e.reason)
			
	sleep(10)

tweet()