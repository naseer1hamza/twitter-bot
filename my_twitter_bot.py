import tweepy
import time
from keys import *


auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def reply_to_tweets():
	print('retriving and replying to tweets...')

	last_seen_id = retrieve_last_seen_id(FILE_NAME)
	mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')

	for i in reversed(mentions):
		print(str(i.id) + ' - ' + i.full_text)
		last_seen_id = i.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		if '#helloworld' in i.full_text.lower():
			print("responding back")
			api.update_status('@' + i.user.screen_name + ' #HellowWorld back to you!', i.id)


while True:
	reply_to_tweets()
	time.sleep(15)

