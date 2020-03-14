import requests

response = requests.get("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"quote\"]{quote,author->{author},source->{source}}")
DictA = response.json()

for key, value in DictA.items():
    print(key)

#{'author': {'author': 'Becky Chambers'}, 'quote': '"Moss green scales sheathed her body from the top of her head to the tip of her tail, fading into a paler shade over her belly."', 'source': {'source': 'The Long way to a Small, Angry Planet'}}