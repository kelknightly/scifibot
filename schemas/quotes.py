import requests
import random

response = requests.get("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"quote\"]{quote,author->{author},source->{source}}")
DictA = response.json()

sentences = []
for result in DictA['result']:
    author = result['author']['author']
    quote = result['quote']
    source = result['source']['source']
    sentence = quote + ' ~ ' + author + ', ' + source
    sentences.append(sentence)

print(random.choice(sentences))
