import requests
import random
import hashlib
import json
from twython import Twython

with open('schemas/scifibot-quote.json') as json_tweets:
    tweet_control = json.load(json_tweets)

response = requests.get("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"quote\"]{quote,author->{author},source->{source}}")
DictA = response.json()

sentences = []
for result in DictA['result']:
    author = result['author']['author']
    quote = result['quote']
    source = result['source']['source']
    sentence = quote + ' ~ ' + author + ', ' + source
    sentences.append(sentence)

tweet = random.choice(sentences)
tweethash = hashlib.md5(tweet.encode('utf-8')).hexdigest()

while tweethash in tweet_control['tweet hashes']:
    tweet = random.choice(tweet)
    tweethash = hashlib.md5(tweet.encode('utf-8')).hexdigest()

tweet_control['tweet hashes'].append(tweethash)
tweet_control['tweet count'] += 1
with open('schemas/scifibot-quote.json', 'w') as outfile:
    json.dump(tweet_control, outfile)

# Load credentials from json file
with open("schemas/twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

twitter.update_status(status=tweet)
print('TWEETED: ', tweet)
quit()