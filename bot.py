#coding=utf-8
import tweepy
from config import AUTH_DATA
from do_oauth import request_access
from tweets import TWEETS

class TweetBot:
    def __init__(self):
        consumer_key = AUTH_DATA['consumer_key']
        consumer_secret = AUTH_DATA['consumer_secret']
        credentials = request_access(consumer_key, consumer_secret)
        token = credentials[0]
        secret = credentials[1]
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(token, secret)
        self.api = tweepy.API(auth)


    def tweet(self, text):
        self.api.update_status(text)

    def random_autotweet(self, tweets, delay):
        pass


if __name__ == '__main__':
    b = TweetBot()
    b.tweet('Hola a todos desde tweepy!.')
