import tweepy
from creds import API_KEY, API_SECRET_KEY
import json
import sys
import pandas as pd
import os

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
api = tweepy.API(auth)

if len(sys.argv) < 2:
    print("Enter at least keyword for your search")
    quit()
tweets = api.search_tweets(q=str(sys.argv[1]), tweet_mode='extended')
for tweet in tweets:
    to_dict = {}
    splitted = tweet.full_text.split(':')
    if "RT @" in splitted[0]:
        continue
    to_dict['tweet_date'] = str(tweet.created_at)
    to_dict['tweet_id'] = tweet.id
    to_dict['tweet_body'] = tweet.full_text
    to_dict['author_username'] = '@' + tweet.author.screen_name
    to_dict['author_name'] = tweet.author.name
    to_dict['author_id'] = tweet.author.id
    with open('{}.json'.format(to_dict['tweet_id']), 'w+') as f:
        f.write(json.dumps(to_dict, indent=4))
    f.close()