import csv
import json

jsons = []

# actions
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_action.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        action = {
            '_id': row[0],
            '_type': 'action',
            'action': row[1],
            'actionType': {
                '_type': 'reference',
                '_ref': row[2]
            }
        }
        jsons.append(json.dumps(action))


# actiontype
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_actiontype.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        action = {
            '_id': row[0],
            '_type': 'actionType',
            'actionType': row[1],
        }
        jsons.append(json.dumps(action))

# noun
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_noun.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        noun = {
            '_id': row[0].replace(' ', ''), 
            '_type': 'noun',
            'noun': row[1],
            'nounType': {
                '_type': 'reference',
                '_ref': row[2]
            }
        }
        jsons.append(json.dumps(noun))


# nountype
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_nountype.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        noun = {
            '_id': row[0],    
            '_type': 'nounType',
            'nounType': row[1],
        }
        jsons.append(json.dumps(noun))


# description
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_description.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        description = {
            '_id': row[0], 
            '_type': 'description',
            'description': row[1],
            'nounType': {
                '_type': 'reference',
                '_ref': row[2]
            }
        }
        jsons.append(json.dumps(description))

# articleword
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_articleword.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        articleword = {
            '_id': row[0].replace(' ', ''), 
            '_type': 'articleword',
            'articleword': row[1],
            'articleType': {
                '_type': 'reference',
                '_ref': row[2]
            }
        }
        jsons.append(json.dumps(articleword))


# articletype
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_articletype.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        articleType = {
            '_id': row[0],    
            '_type': 'articleType',
            'articleType': row[1],
        }
        jsons.append(json.dumps(articleType))


# quote
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_quote.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        quote = {
            '_id': row[0], 
            '_type': 'quote',
            'quote': row[1],
            'author': {
                '_type': 'reference',
                '_ref': row[3]
            },
            'source': {
                '_type': 'reference',
                '_ref': row[2]
            }
        }
        jsons.append(json.dumps(quote))


# source
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_source.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        source = {
            '_id': row[0], 
            '_type': 'source',
            'source': row[1],
            'author': {
                '_type': 'reference',
                '_ref': row[2]
            }
        }
        jsons.append(json.dumps(source))


# author
with open('C:\\Users\\kellt\\OneDrive\\Documents\\scifi_imports_sanity\\sanity_import_author.csv', newline='') as csvfile:
    sanityread = csv.reader(csvfile)
    next(sanityread)
    for row in sanityread:
        author = {
            '_id': row[0],    
            '_type': 'author',
            'author': row[1]
        }
        jsons.append(json.dumps(author))


text_file = open('sanity_ndjson.txt', 'w+')
for json_str in jsons:
    text_file.writelines(json_str + '\n')
text_file.close()    


# sanity dataset delete production
# run import.py
# sanity dataset import sanity_ndjson.txt

# add, commit, push changes in Python

# ssh kelltrill@cloud9ide.bryangruneberg.com
# cd Projects/scifibot
# git pull

#### to see what's been sent ####
# cat ~/logs/scifibot/quotes.log
# cat ~/logs/scifibot/sentencs.log

# ~ means home directory
# ls -la gives a list
# git push on python side, then git pull on cloud9 server
# ctrl + d to get back to your machine