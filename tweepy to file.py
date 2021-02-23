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

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#stream listener tweets_listener
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

#Tweet listening
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["ireland", "sport" ], languages=["en"])


