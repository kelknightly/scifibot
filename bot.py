import requests
import json
import random
import time
import string
import names
import hashlib
from twython import Twython 

# Sentence construction
from scifisanity import scifisanity

bot = scifisanity()


under280 = bot.get_all_sentences(280)

tweet = random.choice(under280)
tweethash = hashlib.md5(tweet.encode('utf-8')).hexdigest()

try:
    with open('scifibot-sentence.json') as json_tweets:
        tweet_control = json.load(json_tweets)
except:
    tweet_control = {
        'tweet hashes': [],
        'tweet count': 0
    }

while tweethash in tweet_control['tweet hashes']:
    tweet = random.choice(under280)
    tweethash = hashlib.md5(tweet.encode('utf-8')).hexdigest()

tweet_control['tweet hashes'].append(tweethash)
tweet_control['tweet count'] += 1

with open('scifibot-sentence.json', 'w') as outfile:
    json.dump(tweet_control, outfile)

# Load credentials from json file
try:
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)
except:
    print("Twitter credentials are missing")
    creds = {
        'CONSUMER_KEY': 'KEY',
        'CONSUMER_SECRET': 'SECRET',
        'ACCESS_TOKEN': 'TOKEN',
        'ACCESS_SECRET': 'SECRET'
    }

# Instantiate an object
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

try:
    twitter.update_status(status=tweet)
    print('Tweet sent:', tweet)
except:
    print('Tweet not sent:', tweet)
