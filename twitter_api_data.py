#import package
import tweepy
import json

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ZhsGFGA6twuzFT9ZH99K16E48",
    "aYwVl9eikRXYylcQB0xxp3FUz2oYTrY3xsGARmMkbr4GMJMhLP")
#tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token("1347989941024940032-wTj6f6tT34oL2slakxKvk6xFKUYLSg",
    "g35B5svvrVkzE1n6jmNwC7hrTsfuhAzA6EVmC4t2eDj48")
#auth.set_access_token(access_token,access_token_secret)
# Create API object
api = tweepy.API(auth)


 #Streaming Tweets
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

# Initialize Stream listener
tweets_listener = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, tweets_listener)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(track = ['ireland', 'rugby'])
