import requests
import json
import random

def extracting(query):
    response = requests.get(query)
    DictA = response.json()

    query_list = list(DictA.values())
    query_list = query_list[2]

    val_list = []
    val_key = []
    counter = 0
    for i in query_list:
        val = i.values()
        for i in val:
            counter += 1
            if counter % 2 != 0:
                val_list.append(i)
            if counter % 2 == 0:
                key = i.values()
                for i in key:
                    val_key.append(i)

    zipped = dict(zip(val_list, val_key))
    return zipped

nouns = extracting("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"noun\"]{noun,nounType->{nounType}}")
actions = extracting("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"action\"]{action,actionType->{actionType}}")
descriptions = extracting("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"description\"]{description,nounType->{nounType}}")

# Categorising function to splut out the key, value pairs
def categorising(valuetype, value):
    ListA = []
    for key, val in valuetype.items():
        if val == value:
            ListA.append(key)
    return ListA

# Passing content type values into categorising function
list_primary_actor = categorising(nouns, 'primary actor')
list_secondary_actor = categorising(nouns, 'secondary actor')
list_actor = list_primary_actor + list_secondary_actor
list_in_place = categorising(nouns, 'in-place')
list_on_place = categorising(nouns, 'on-place')
list_place = list_in_place + list_on_place
list_in_place_description = categorising(descriptions, 'in-place')
list_on_place_description = categorising(descriptions, 'on-place')
list_place_description = list_in_place_description + list_on_place_description
list_place_action = categorising(actions, 'place')
list_weapon = categorising(nouns, 'weapon')
list_transport = categorising(nouns, 'transport')
list_weapon_action = categorising(actions, 'weapon')
list_transport_action = categorising(actions, 'transport')
list_sentient_positive_action = categorising(actions, 'sentient positive')
list_sentient_negative_action = categorising(actions, 'sentient negative')
list_sentient_action = list_sentient_positive_action + list_sentient_negative_action
list_primary_actor_description = categorising(descriptions, 'primary actor')
list_secondary_actor_description = categorising(descriptions, 'secondary actor')
list_actor_description = list_primary_actor_description + list_secondary_actor_description
list_weapon_description = categorising(descriptions, 'weapon')
list_transport_description = categorising(descriptions, 'transport')
list_transport_function = categorising(actions, 'transport function')
list_transport_damage_action = categorising(actions, 'transport damage')
list_transport_equipped = categorising(descriptions, 'transport after')
list_transport_damage_noun = categorising(nouns, 'transport damage')
list_regime = categorising(nouns, 'politics')
list_group = categorising(nouns, 'group')
list_civilisation = categorising(descriptions, 'civilisation')
list_secondary_actor_plural = categorising(nouns, 'secondary actors plural')


# Randomly selecting a word within each list
in_place = random.choice(list_in_place)
on_place = random.choice(list_on_place)
place = random.choice(list_place)
place_action = random.choice(list_place_action)
place_desc = random.choice(list_place_description)
secondary_actor = random.choice(list_secondary_actor)
primary_actor = random.choice(list_primary_actor)
weapon_action = random.choice(list_weapon_action)
transport_action = random.choice(list_transport_action)
sentient_positive_action = random.choice(list_sentient_positive_action)
sentient_negative_action = random.choice(list_sentient_negative_action)
sentient_action = random.choice(list_sentient_action)
primary_actor_desc = random.choice(list_primary_actor_description)
secondary_actor_desc = random.choice(list_secondary_actor_description)
weapon_desc = random.choice(list_weapon_description)
transport_desc = random.choice(list_transport_description)
weapon = random.choice(list_weapon)
transport = random.choice(list_transport)
actor = random.choice(list_actor)
actor_desc = random.choice(list_actor_description)
transport_function = random.choice(list_transport_function)
transport_damage_action = random.choice(list_transport_damage_action)
transport_equipped = random.choice(list_transport_equipped)
transport_damage_noun = random.choice(list_transport_damage_noun)
regime = random.choice(list_regime)
group = random.choice(list_group)
civilisation = random.choice(list_civilisation)
secondary_actors = random.choice(list_secondary_actor_plural)

# Randomising a second time for variables that are used twice in a sentence
place2 = random.choice(list_place)
secondary_actor2 = random.choice(list_secondary_actor)
transport_equipped2 = random.choice(list_transport_equipped)

def randomiser_duplicator(val1, val2, val_list):

    while val1 == val2:
        val2 = random.choice(val_list)
        if val1 != val2:
            break
            #return val1, val2

randomiser_duplicator(place, place2, list_place)
randomiser_duplicator(secondary_actor, secondary_actor2, list_secondary_actor)
randomiser_duplicator(transport_equipped, transport_equipped2, list_transport_equipped)
print(place, place2)
print(secondary_actor, secondary_actor2)
print(transport_equipped, transport_equipped2)

# Function to place 'a' or 'an' before a noun
def article(component):
    if component[0] in ('a','e','i','o','u'):
        article = 'an'
    else: 
        article = 'a'
    return article

primary_actor_article = article(primary_actor_desc)
secondary_actor_article = article(secondary_actor_desc)
place_article = article(place_desc)
weapon_article = article(weapon_desc)
transport_article = article(transport_desc)
actor_article = article(actor)
civilisation_article = article(civilisation)
secondary_actor2_article = article(secondary_actor2)
place2_article = article(place2)

# Listing prepositions
list_weapon_preposition = ['with', 'using']
weapon_preposition = random.choice(list_weapon_preposition)
list_transport_preposition = ['aboard', 'on']
transport_preposition = random.choice(list_transport_preposition)

list_looking_for = ['food', 'revenge', 'love', 'supplies', 'help', 'adventure']
looking_for = random.choice(list_looking_for)

# Sentence construction - Model 1 Phrase 1
structure1 = primary_actor_article.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_action + ' ' + secondary_actor_article + ' ' + secondary_actor_desc + ' ' + secondary_actor + '.'
structure2 = primary_actor_article.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_action + ' ' + secondary_actor_article + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' ' + transport_preposition + ' ' + transport_article + ' ' + transport_desc + ' ' + transport + '.'
structure3 = primary_actor_article.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_negative_action + ' ' + secondary_actor_article + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' ' + weapon_preposition + ' ' + weapon_article + ' ' + weapon_desc + ' ' + weapon + '.'
structure4_1 = primary_actor_article.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_action + ' ' + secondary_actor_article + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' in ' + place_article + ' ' + place_desc + ' ' + in_place + '.'
structure4_2 = primary_actor_article.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_action + ' ' + secondary_actor_article + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' on ' + place_article + ' ' + place_desc + ' ' + on_place + '.'
structure5 = primary_actor_article.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + place_action + ' ' + place_article + ' ' + place_desc + ' ' + place + '.'
structure6 = primary_actor_article.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + transport_preposition + ' ' + transport_article + ' ' + transport_desc + ' ' + transport + ' ' + place_action + ' ' + place_article + ' ' + place_desc + ' ' + place + '.'
structure7 = secondary_actor_article.title() + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' from ' + place_article + ' ' + place_desc + ' ' + place + ' ' + weapon_action + ' ' + weapon_article + ' ' + weapon_desc + ' ' + weapon + '.'
structure8 = secondary_actor_article.title() + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' ' + sentient_negative_action + ' ' + primary_actor_article + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + weapon_preposition + ' ' + weapon_article + ' ' + weapon_desc + ' ' + weapon + '.'
structure9 = primary_actor_article.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + transport_action + ' ' + transport_article + ' ' + transport_desc + ' ' + transport + '.'
structure10 = actor_article.title() + ' ' + actor_desc + ' ' + actor + ' ' + place_action + ' ' + place_article + ' ' + place_desc + ' ' + place

structure11 = place_article.title() + ' ' + place_desc + ' ' + place + ' orbits ' + place2_article + ' ' + place2 + '. It is home to a ' + group + ' ' + secondary_actor_desc + ' ' + secondary_actors + ' looking for ' + looking_for + '.'

if place == 'civilisation':
    civ_soc = 'society'
else:
    civ_soc = 'civilisation'

structure12 = place_article.title() + ' ' + place_desc + ' ' + place + ' is home to a ' + civilisation + ' ' + civ_soc + ' of ' + secondary_actors + '. They have acquired ' + weapon_article + ' ' + weapon_desc + ' ' + weapon + ' and will use it for war.'

structure13 = 'You have stumbled upon ' + transport_article + ' ' + transport_desc + ' ' + transport + ' from ' + regime + '. It is equipped with ' + transport_equipped + ' and ' + transport_equipped2 + '.'
#print(structure13)

tweets = []
tweets.extend([structure1, structure2, structure3, structure4_1, structure4_2, structure5, structure6, structure7, structure8, structure9, structure10, structure11, structure12])

############################################
# Selecting a random structure for the tweet
############################################
#print(random.choice(tweets))
############################################


from random_word import RandomWords
import random
r_word = RandomWords()
r_word = r_word.get_random_word(includePartOfSpeech='noun', maxLength=10)

r_num = random.randint(100,999)

#print('Planet ' + r_word.title()+str(r_num))

import string

r_str = ''.join(random.choice(string.ascii_letters) for x in range(5))
#print(r_str)
