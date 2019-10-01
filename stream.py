import os
import sys
import json
import tweepy
from dotenv import load_dotenv
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# Load credentials from .env file
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authentication
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# Create API instance
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False
        

twitter_stream = MyStreamListener()

stream = tweepy.Stream(auth, twitter_stream)
for status in tweepy.Cursor(api.user_timeline).items(200):
    print(status.text)
#stream.filter(follow=["1036857185408569345"])