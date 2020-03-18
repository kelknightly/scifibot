import requests
import json
import random
import time
import string
import names
import hashlib
from twython import Twython


with open('schemas/scifibot-sentence.json') as json_tweets:
    tweet_control = json.load(json_tweets)

def get_noun_list(query):
    response = requests.get(query)
    DictA = response.json()
    nouns = []
    for result in DictA['result']:
        nouns.append({
            "noun": result['noun'],
            "type": result['nounType']['nounType']
        })
    return(nouns)

def get_noun_list_for_type(nouns, nounType_filter):
    noun_list = []
    for noun in nouns:
        if noun['type'] == nounType_filter:
            noun_list.append(noun['noun'])
    return noun_list


def get_description_list(query):
    response = requests.get(query)
    DictA = response.json()
    descriptions = []
    for result in DictA['result']:
        descriptions.append({
            "description": result['description'],
            "type": result['nounType']['nounType']
        })
    return(descriptions)

def get_description_list_for_type(descriptions, nounType_filter):
    description_list = []
    for description in descriptions:
        if description['type'] == nounType_filter:
            description_list.append(description['description'])
    return description_list


def get_action_list(query):
    response = requests.get(query)
    DictA = response.json()
    actions = []
    for result in DictA['result']:
        actions.append({
            "action": result['action'],
            "type": result['actionType']['actionType']
        })
    return(actions)

def get_action_list_for_type(actions, actionType_filter):
    action_list = []
    for action in actions:
        if action['type'] == actionType_filter:
            action_list.append(action['action'])
    return action_list

def bruteForceRandomWord(part, length):
    url = "https://wordsapiv1.p.rapidapi.com/words/"
    querystring = {"random":"true"}
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "d13b08e2c9mshdb21833bede88e1p13c577jsn79fe44d0a6f9"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    js = response.json()
    return js['word']

nouns = get_noun_list("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"noun\"]{noun,nounType->{nounType}}")
descriptions = get_description_list("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"description\"]{description,nounType->{nounType}}")
actions = get_action_list("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"action\"]{action,actionType->{actionType}}")

# Getting lists of Nouns
list_primary_actor = get_noun_list_for_type(nouns, 'primary actor')
list_secondary_actor = get_noun_list_for_type(nouns, 'secondary actor')
list_actor = list_primary_actor + list_secondary_actor
list_in_place = get_noun_list_for_type(nouns, 'in-place')
list_on_place = get_noun_list_for_type(nouns, 'on-place')
list_place = list_in_place + list_on_place
list_weapon = get_noun_list_for_type(nouns, 'weapon')
list_transport = get_noun_list_for_type(nouns, 'transport')
list_transport_damage_noun = get_noun_list_for_type(nouns, 'transport damage')
list_regime = get_noun_list_for_type(nouns, 'politics')
list_group = get_noun_list_for_type(nouns, 'group')
list_secondary_actor_plural = get_noun_list_for_type(nouns, 'secondary actors plural')
list_measuring_things = get_noun_list_for_type(nouns, 'measuring')
list_liquid = get_noun_list_for_type(nouns, 'liquid')
list_tech = get_noun_list_for_type(nouns, 'tech')
list_transport_name = get_noun_list_for_type(nouns, 'transport name')
list_transports = get_noun_list_for_type(nouns, 'transport plural')
list_engine = get_noun_list_for_type(nouns, 'engine')

# Getting lists of Descriptions
list_in_place_description = get_description_list_for_type(descriptions, 'in-place')
list_on_place_description = get_description_list_for_type(descriptions, 'on-place')
list_place_description = list_in_place_description + list_on_place_description
list_primary_actor_description = get_description_list_for_type(descriptions, 'primary actor')
list_secondary_actor_description = get_description_list_for_type(descriptions, 'secondary actor')
list_actor_description = list_primary_actor_description + list_secondary_actor_description
list_weapon_description = get_description_list_for_type(descriptions, 'weapon')
list_transport_description = get_description_list_for_type(descriptions, 'transport')
list_transport_equipped = get_description_list_for_type(descriptions, 'transport equipped')
list_a__society = get_description_list_for_type(descriptions, 'a__society')
list_liquid_desc = get_description_list_for_type(descriptions, 'liquid')
list_society_is_a__ = get_description_list_for_type(descriptions, 'society_is_a__')
list_crust = get_description_list_for_type(descriptions, 'crust')
list_sky = get_description_list_for_type(descriptions, 'sky')
list_transport_name_desc = get_description_list_for_type(descriptions, 'transport name')

# Getting lists of Actions
list_place_action = get_action_list_for_type(actions, 'place')
list_weapon_action = get_action_list_for_type(actions, 'weapon')
list_transport_action = get_action_list_for_type(actions, 'transport')
list_sentient_positive_action = get_action_list_for_type(actions, 'sentient positive')
list_sentient_negative_action = get_action_list_for_type(actions, 'sentient negative')
list_sentient_action = list_sentient_positive_action + list_sentient_negative_action
list_transport_function = get_action_list_for_type(actions, 'transport function')
list_transport_damage_action = get_action_list_for_type(actions, 'transport damage')
list_suddenly = get_action_list_for_type(actions, 'suddenly')
list_sentient_action_plural = get_action_list_for_type(actions, 'sentient plural')
list_transport_about = get_action_list_for_type(actions, 'transport about')
list_looking_for = get_action_list_for_type(actions, 'looking for')

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
a__society = random.choice(list_a__society)
secondary_actors = random.choice(list_secondary_actor_plural)
measuring_things = random.choice(list_measuring_things)
suddenly = random.choice(list_suddenly)
liquid = random.choice(list_liquid)
liquid_desc = random.choice(list_liquid_desc)
sentient_action_plural = random.choice(list_sentient_action_plural)
society_is_a__ = random.choice(list_society_is_a__)
tech = random.choice(list_tech)
crust = random.choice(list_crust)
sky = random.choice(list_sky)
transport_name_noun = random.choice(list_transport_name)
transport_name_desc = random.choice(list_transport_name_desc)
transport_about = random.choice(list_transport_about)
transports = random.choice(list_transports)
engine = random.choice(list_engine)
looking_for = random.choice(list_looking_for)

# Randomising a second time for variables that are used twice in a sentence
place2 = random.choice(list_place)
place2_desc = random.choice(list_place_description)
secondary_actor2 = random.choice(list_secondary_actor)
transport_equipped2 = random.choice(list_transport_equipped)
transport_function2 = random.choice(list_transport_function)
secondary_actor_desc2 = random.choice(list_secondary_actor_description)
primary_actor2 = random.choice(list_primary_actor)

def randomiser_duplicator(val1, val2, val_list):
    while val1 == val2:
        val2 = random.choice(val_list)
        if val1 != val2:
            return val2
    return val2

place2 = randomiser_duplicator(place, place2, list_place)
place2_desc = randomiser_duplicator(place_desc, place2_desc, list_place_description)
secondary_actor2 = randomiser_duplicator(secondary_actor, secondary_actor2, list_secondary_actor)
transport_equipped2 = randomiser_duplicator(transport_equipped, transport_equipped2, list_transport_equipped)
transport_function2 = randomiser_duplicator(transport_function, transport_function2, list_transport_function)
secondary_actor_desc2 = randomiser_duplicator(secondary_actor_desc, secondary_actor_desc2, list_secondary_actor_description)
primary_actor2 = randomiser_duplicator(primary_actor, primary_actor2, list_primary_actor)

# Function to place 'a' or 'an' before a noun
def article(i):
    if i[0] in ('a','e','i','o','u','A','E','I','O','U'):
        article = 'an'
    elif i in ('useless','euphoric','euphemism','usurper','eunuch','eulogy','upsilon meson','eugenist','Ukrainian','utilitarian'):
        article = 'a'
    else: 
        article = 'a'
    return article

primary_actor_article_on_desc = article(primary_actor_desc)
secondary_actor_article_on_desc = article(secondary_actor_desc)
place_article_on_desc = article(place_desc)
weapon_article_on_desc = article(weapon_desc)
transport_article_on_desc = article(transport_desc)
actor_article_on_desc = article(actor_desc)
primary_actor_article = article(primary_actor)
secondary_actor_article = article(secondary_actor)
place_article = article(place)
weapon_article = article(weapon)
transport_article = article(transport)
actor_article = article(actor)
a__society_article = article(list_a__society)
secondary_actor2_article = article(secondary_actor2)
place2_article = article(place2)
primary_actor2_article = article(primary_actor2)
place2_article_on_desc = article(place2_desc)
society_is_a__article = article(society_is_a__)
crust_article = article(crust)
engine_article = article(engine)

# Listing prepositions
list_weapon_preposition = ['with', 'using']
weapon_preposition = random.choice(list_weapon_preposition)
list_transport_preposition = ['aboard', 'on']
transport_preposition = random.choice(list_transport_preposition)

if place in list_in_place:
    place_prep = 'in'
if place in list_on_place:
    place_prep = 'on'

list_pronoun = ['she', 'he']
pronoun = random.choice(list_pronoun)
# possessive pronoun
if pronoun == 'she':
    pos_pro = 'her'
if pronoun == 'he':
    pos_pro = 'his'

list_planetsystemsector = ['Planet', 'System', 'Sector']
planetsystemsector = random.choice(list_planetsystemsector)

measuring = ['measuring', 'considering', 'tracking']
measuring = random.choice(measuring)
        
verb = bruteForceRandomWord('verb', 10)
noun1 = bruteForceRandomWord('noun', 10)
noun2 = bruteForceRandomWord('noun', 10)
name = verb.title() + ' ' + noun1.title() + ' the ' + noun2.title()

# Sentence construction

structure1 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' named \'' + name + '\' ' + sentient_action + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + '.'
structure2 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_negative_action + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' ' + transport_preposition + ' ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + '.'
structure3 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' with ' + weapon_article_on_desc + ' ' + weapon_desc + ' ' + weapon + ' ' + sentient_negative_action + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + '.'
structure4 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_action + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' ' + place_prep + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '.'
structure5 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + place_action + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '.'
structure7 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + transport_preposition + ' ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' ' + place_action + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '.'
structure8 = primary_actor_article_on_desc.title() + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' from ' + place_article_on_desc + ' ' + place_desc + ' ' + place + ' ' + weapon_action + ' ' + weapon_article_on_desc + ' ' + weapon_desc + ' ' + weapon + '.'
structure9 = actor_article_on_desc.title() + ' ' + actor_desc + ' ' + actor + ' ' + place_action + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '. History will remark on this for generations.'
structure10 = actor_article_on_desc.title() + ' ' + actor_desc + ' ' + actor + ' ' + place_action + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '. Lifetimes will pass before this moment is forgotten.'
structure11 = place_article_on_desc.title() + ' ' + place_desc + ' ' + place + ' orbits ' + place2_article + ' ' + place2 + '. It is home to a ' + group + ' ' + secondary_actor_desc + ' ' + secondary_actors + ' looking for ' + looking_for + '.'

if place == 'civilisation':
    civ_soc = 'society'
else:
    civ_soc = 'civilisation'

structure12 = place_article_on_desc.title() + ' ' + place_desc + ' ' + place + ' is home to ' + a__society_article + ' ' + a__society + ' ' + civ_soc + ' of ' + secondary_actors + '. They have acquired ' + weapon_article_on_desc + ' ' + weapon_desc + ' ' + weapon + ' and will use it for war.'
structure13 = 'You have stumbled upon ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' from ' + regime + '. It is equipped with ' + transport_equipped + ', and ' + transport_equipped2 + '.'
structure14 = 'You have stumbled upon ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' from ' + regime + '. With ' + engine_article + ' ' + engine + ' ' + ', it is one of the most powerful ships in the galaxy.'
structure15 = 'You are the Captain of ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' from ' + regime + '. It has a dual function: ' + transport_function + ', and ' + transport_function2 + '.'
structure16 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' manoeuvres ' + transport_article + ' ' + transport + '. ' + pronoun.title() + '\'s been hired to protect ' +  planetsystemsector + ' ' + bruteForceRandomWord('noun', 10).title()+str(random.randint(100,999)) + ' from invaders.'
structure17 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' drifts helplessly in empty space. ' + pos_pro.title() + ' ' + transport + ' has been damaged by ' + transport_damage_noun + ' and ' + pronoun + ' needs immediate assistance.'
structure18 = place_article_on_desc.title() + ' ' + place_desc + ' ' + place + ' flies through space driven by ' + engine_article + ' ' + engine + '.'
structure19 = 'Several ' + secondary_actor_desc + ' ' + secondary_actors + ' drift in empty space. They made a bad miscalculation.'
structure20 = 'Several ' + secondary_actor_desc + ' ' + secondary_actors + ' drift in empty space. They screwed the pooch on this one.'
structure21 = 'Several ' + secondary_actor_desc + ' ' + secondary_actors + ' drift in empty space. They fucked up.'
structure22 = 'Several ' + secondary_actor_desc + ' ' + secondary_actors + ' drift in empty space, much too far to be rescued. They are alone.'
structure23 = primary_actor_article.title() + ' ' + primary_actor + ', codename ' + (''.join(random.choice(string.ascii_letters) for x in range(5))) + ', has been hired to abduct or kill ' + primary_actor_article_on_desc + ' ' + primary_actor_desc + ' ' + primary_actor2 + ', but needs ' + weapon_article_on_desc + ' ' + weapon_desc + ' ' + weapon + ' to complete the job.'
structure24 = regime.title() + ' has tasked you with tracking, capturing, and returning ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' lost ' + place_prep + ' a distant ' + place + '. It will take all your skills as ' + primary_actor_article + ' ' + primary_actor + '.'
structure25 = secondary_actor_article_on_desc.title() + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' orbits ' + place_article_on_desc + ' ' + place_desc + ' ' + place + ', ' + measuring + ' ' + measuring_things + '.'
structure26 = transport_article_on_desc.title() + ' ' + transport_desc + ' ' + transport + ' you assumed to be friendly suddenly ' + suddenly + '.'

list_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
liquid_type = random.choice(['it rains', 'there are deep oceans of', 'there are clouds of', 'there are pools of', 'rivers run with', 'the skies are full of', 'there is an ocean of'])

structure27 = str(random.randint(100,999)) + ' ' + 'light years away on the planet' + ' ' + bruteForceRandomWord('noun', 10).upper() + '-' + str(random.randint(1,100)) + random.choice(list_alpha) + ', ' + liquid_type + ' ' + liquid_desc + ' ' + liquid + '.'
structure28 = 'I was ' + sentient_action_plural + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' the day the ' + secondary_actors + ' attacked. ' 
structure29 = 'I was ' + sentient_action_plural + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' from ' + place_article_on_desc + ' ' + place_desc + ' ' + place + ' the day the ' + secondary_actors + ' attacked. ' 

person_title = random.choice(['Ms', 'Mr', 'Dr'])
structure30 = 'Belay my previous order, ' + person_title + ' ' + string.capwords(bruteForceRandomWord('noun', 10)) + '. We need a vital show of force. Activate the ' + weapon_desc + ' ' + weapon + ' and aim it at the ' + place + '.'

structure31 = 'The border outpost reports a contingent of ' + str(random.randint(2,20)) + ' ' + secondary_actor + ' ' + transports + ' within sensor range. Should hostilities erupt, we will be outgunned.'
structure32 = 'The border outpost reports a contingent of ' + str(random.randint(2,20)) + ' ' + secondary_actor + ' ' + transports + ' within sensor range. We should try to maintain diplomatic relations.'

stardate = str(random.randint(1000, 56947)) + '.' + str(random.randint(1,9))
system_name = bruteForceRandomWord('noun', 5) + ' ' + bruteForceRandomWord('noun', 5)
structure33 = 'Captain\'s Log, Stardate ' + stardate + '. We are cautiously entering the ' + string.capwords(system_name) + ' star system, ' + str(random.randint(2,20)) + ' days after receiving a distress call from '+ regime + ' colony. The garbled transmission reported the colony under attack.'
structure34 = 'Captain\'s log, Stardate ' + stardate + '. Admiral ' + names.get_first_name() + ' and Lieutenant Commander ' + names.get_first_name() + ' of Starfleet Tactical have arrived to review the disappearance of New ' + bruteForceRandomWord('noun', 10).title() + ' colony. No sign remains of the ' + str(random.randint(100,1000)) + ' inhabitants.'

roman_numeral = random.choice(['I','II','III','IV','V','VI','VII','VIII','X'])
structure35 = 'Captain\'s Log, Stardate ' + stardate + '. We\'ve been ordered to Starbase ' +  str(random.randint(10,90)) + ' in orbit around ' + bruteForceRandomWord('noun', 10).title() + ' ' + roman_numeral + '. The ' + weapon_desc.title() + ' ' + weapon.title() + ' has been glitching and needs an urgent upgrade before another crewmember dies.'
structure36 = actor_article_on_desc.title() + ' ' + actor_desc + ' ' + actor + ' drifts in empty space, following the path of a particular ' + secondary_actor +' through space-time.'
structure37 = place_article_on_desc.title() + ' ' + place_desc + ' ' + place + ' orbits ' + place2_article_on_desc + ' ' + place2_desc + ' ' + place2 + '. Raging storms of ' + liquid_desc + ' ' + liquid + ' fill its skies.'
structure38 = 'NASA has discovered an inhabited exoplanet. The society appears to be ' + society_is_a__article + ' ' + society_is_a__ + ', and early scans reveal advanced ' + tech + ' and ' + crust_article + ' ' + crust + ' crust. The sky is ' + sky + ' and a day lasts ' + str(random.randint(2,100)) + ' Earth hours.'
structure39 = 'Your mission is to document a strange planet\'s surface. The society appears to be ' + society_is_a__article + ' ' + society_is_a__ + ', and early scans reveal advanced ' + tech + ' and ' + crust_article + ' ' + crust + ' crust. The sky is ' + sky + ' and a day lasts ' + str(random.randint(2,100)) + ' Earth hours.'
structure40 = 'You encounter ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' with the words \'' + string.capwords(transport_name_desc) + ' ' + string.capwords(transport_name_noun) + '\' painted on the side. It ' + transport_about + ' and is equipped with ' + transport_equipped + '.'
structure41 = 'The ' + transport_desc + ' ' + transport + ' you\'ve encountered ' + transport_about + '. It seems to have a bad ' + secondary_actor + ' infestation, so probably best to steer clear of it.'
structure42 = 'You are the Commander of ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' and have decided to name it \'' + string.capwords(transport_name_desc) + ' ' + string.capwords(transport_name_noun) + '\'. It has a dual function: ' + transport_function + ', and ' + transport_function2 + '.'
structure43 = 'You are the Commander of ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' and have decided to name it \'' + string.capwords(transport_name_desc) + ' ' + string.capwords(transport_name_noun) + '\'. It ' + transport_about  + ' and is the pride of ' + regime + '.'
structure44 = a__society_article.title() + ' ' + a__society + ' ' + civ_soc + ' is involved in the business of relocating ' + place_article_on_desc + ' ' + place_desc + ' ' + place + ' using ' + engine_article + ' ' + engine + '.'
structure45 = 'You have stumbled upon ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' from ' + regime + '. It is equipped with ' + transport_equipped + ' and boasts ' + engine_article + ' ' + engine + '.'
structure46 = transport_article_on_desc.title() + ' ' + transport_desc + ' ' + transport + ' looms in the distant blackness of space. Its ' + engine + ' flares, and the ' + secondary_actors + ' onboard prepare for battle.'
structure47 = 'The ' + secondary_actors + ' onboard the distant ' + transport_desc + ' ' + transport + ' have the taste for human flesh. The ' + engine + ' on their ship is powerful.'
structure48 = 'The ' + secondary_actors + ' onboard the distant ' + transport_desc + ' ' + transport + ' have the taste for human flesh. The ' + engine + ' on their ship is powerful. The human race will come to an end tonight.'
structure49 = 'The ' + secondary_actors + ' onboard the distant ' + transport_desc + ' ' + transport + ' have the taste for human flesh. The ' + engine + ' on their ship is powerful. The human race faces exinction tonight.'
structure50 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' drifts helplessly in space. ' + pronoun.title() + ' is unconscious, and ' + pos_pro + ' ' + transport + ' is ' + transport_damage_action + '.'
structure51 = transport_article_on_desc.title() + ' ' + transport_desc + ' ' + transport + ' orbits ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '. Its ' + secondary_actor_desc + ' inhabitants have tamed a ' + group + ' ' + secondary_actor_desc2 +  ' ' + secondary_actors + '.'
structure52 = primary_actor_article.title() + ' ' + primary_actor + ', codename ' + (''.join(random.choice(string.ascii_letters) for x in range(5))) + ', has been hired to abduct or kill ' + primary_actor_article_on_desc + ' ' + primary_actor_desc + ' ' + primary_actor2 + ', but needs ' + weapon_article_on_desc + ' ' + weapon_desc + ' ' + weapon + ' to create a distraction.'
structure53 = 'We\'re taking a short detour to explore a port with a neutral market. Apparently you can get anything there. We hope to get a good deal on ' + transport_equipped + ' for our ' + transport + '.'
structure54 = 'The ' + secondary_actors + ' onboard the distant ' + transport_desc + ' ' + transport + ' have the taste for human flesh. The ' + engine + ' on their ship is powerful. Run.'

physical_space = ['valley', 'cavern', 'cave', 'crevasse']
structure55 = 'In a shocking finding, scientists have discovered a ' + group + ' ' + secondary_actors + ' living in a previously unexplored ' + random.choice(physical_space) + '. Even more surprising to the researchers is the fact that the ' + secondary_actors + ' appear to be both ' + primary_actor_desc + ' and ' + secondary_actor_desc + '.'
tweets = []
tweets.extend([structure1, structure2, structure3, structure4, structure5, structure7, structure8, structure9, structure10, structure11, structure12, structure13, structure14, structure15, structure16, structure17, structure18, structure19, structure20, structure21, structure22, structure23, structure24, structure25, structure26, structure27, structure28, structure29, structure30, structure31, structure32, structure33, structure34, structure35, structure36, structure37, structure38, structure39, structure40, structure41, structure42, structure43, structure44, structure45, structure46, structure47, structure48, structure49, structure50, structure51, structure52, structure53, structure54, structure55])

under280 = []
for i in tweets:
    if len(i) <= 280:
        under280.append(i)

tweet = random.choice(under280)
tweethash = hashlib.md5(tweet.encode('utf-8')).hexdigest()

while tweethash in tweet_control['tweet hashes']:
    tweet = random.choice(under280)
    tweethash = hashlib.md5(tweet.encode('utf-8')).hexdigest()

tweet_control['tweet hashes'].append(tweethash)
tweet_control['tweet count'] += 1
with open('schemas/scifibot-sentence.json', 'w') as outfile:
    json.dump(tweet_control, outfile)

# Load credentials from json file
with open("schemas/twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

twitter.update_status(status=tweet)
print('TWEETED: ', tweet)
quit()

print('------------------------')

print(
'1: ', structure1, '\n'
'2: ', structure2, '\n'
'3: ', structure3, '\n'
'4: ', structure4, '\n'
'5: ', structure5, '\n' 
'7: ', structure7, '\n' 
'8: ', structure8, '\n' 
'9: ', structure9, '\n' 
'10: ', structure10, '\n'
'11: ', structure11, '\n'
'12: ', structure12, '\n' 
'13: ', structure13, '\n'
'14: ', structure14, '\n'
'15: ', structure15, '\n'
'16: ', structure16, '\n'
'17: ', structure17, '\n'
'18: ', structure18, '\n'
'19: ', structure19, '\n'
'20: ', structure20, '\n'
'21: ', structure21, '\n'
'22: ', structure22, '\n'
'23: ', structure23, '\n'
'24: ', structure24, '\n'
'25: ', structure25, '\n'
'26: ', structure26, '\n'
'27: ', structure27, '\n'
'28: ', structure28, '\n'
'29: ', structure29, '\n'
'30: ', structure30, '\n'
'31: ', structure31, '\n'
'32: ', structure32, '\n'
'33: ', structure33,'\n'
'34: ', structure34, '\n'
'35: ', structure35, '\n'
'36: ', structure36, '\n'
'37: ', structure37, '\n'
'38: ', structure38, '\n'
'39: ', structure39, '\n'
'40: ', structure40, '\n'
'41: ', structure41, '\n'
'42: ', structure42, '\n'
'43: ', structure43, '\n'
'44: ', structure44, '\n'
'45: ', structure45, '\n'
'46: ', structure46, '\n'
'47: ', structure47, '\n'
'48: ', structure48, '\n'
'49: ', structure49, '\n'
'50: ', structure50, '\n'
'51: ', structure51, '\n'
'52: ', structure52, '\n'
'53: ', structure53, '\n'
'54: ', structure54
)