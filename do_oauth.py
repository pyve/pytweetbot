#coding=utf-8
import tweepy

def request_access(key, secret):
    auth = tweepy.OAuthHandler(key, secret)
    auth_url = auth.get_authorization_url()
    print 'Please authorize: ' + auth_url
    verifier = raw_input('PIN: ').strip()
    auth.get_access_token(verifier)
    return (auth.access_token.key, auth.access_token.secret)

