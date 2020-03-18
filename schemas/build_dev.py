import requests
import json
import random
import time
import string
import names

# Sentence construction
from scifisanity import scifisanity
bot = scifisanity()
bot.print_all_sentences()

quit()

structure1 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' named \'' + name + '\' ' + sentient_action + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + '.'
structure2 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_negative_action + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' ' + transport_preposition + ' ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + '.'
structure3 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' with ' + weapon_article_on_desc + ' ' + weapon_desc + ' ' + weapon + ' ' + sentient_negative_action + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + '.'
structure4 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + sentient_action + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' ' + place_prep + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '.'
structure5 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + place_action + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '.'
structure7 = primary_actor_article_on_desc.title() + ' ' + primary_actor_desc + ' ' + primary_actor + ' ' + transport_preposition + ' ' + transport_article_on_desc + ' ' + transport_desc + ' ' + transport + ' ' + place_action + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '.'
structure8 = secondary_actor_article_on_desc.title() + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' from ' + place_article_on_desc + ' ' + place_desc + ' ' + place + ' ' + weapon_action + ' ' + weapon_article_on_desc + ' ' + weapon_desc + ' ' + weapon + '.'
structure9 = actor_article_on_desc.title() + ' ' + actor_desc + ' ' + actor + ' ' + place_action + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '. History will remark on this for generations.'
structure10 = actor_article_on_desc.title() + ' ' + actor_desc + ' ' + actor + ' ' + place_action + ' ' + place_article_on_desc + ' ' + place_desc + ' ' + place + '. Lifetimes will pass before this moment is forgotten.'
structure11 = place_article_on_desc.title() + ' ' + place_desc + ' ' + place + ' orbits ' + place2_article + ' ' + place2 + '. It is home to a ' + group + ' ' + secondary_actor_desc + ' ' + secondary_actors + ' looking for ' + looking_for + '.'


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


structure27 = str(random.randint(100,999)) + ' ' + 'light years away on the planet' + ' ' + bruteForceRandomWord('noun', 10).upper() + '-' + str(random.randint(1,100)) + random.choice(list_alpha) + ', ' + liquid_type + ' ' + liquid_desc + ' ' + liquid + '.'
structure28 = 'I was ' + sentient_action_plural + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' the day the ' + secondary_actors + ' attacked. ' 
structure29 = 'I was ' + sentient_action_plural + ' ' + secondary_actor_article_on_desc + ' ' + secondary_actor_desc + ' ' + secondary_actor + ' from ' + place_article_on_desc + ' ' + place_desc + ' ' + place + ' the day the ' + secondary_actors + ' attacked. ' 

person_title = random.choice(['Ms', 'Mr', 'Dr'])
structure30 = 'Belay my previous order, ' + person_title + ' ' + string.capwords(bruteForceRandomWord('noun', 10)) + '. We need a vital show of force. Activate the ' + weapon_desc + ' ' + weapon + ' and aim it at the ' + place + '.'

structure31 = 'The border outpost reports a contingent of ' + str(random.randint(2,20)) + ' ' + secondary_actor + ' ' + transports + ' within sensor range. Should hostilities erupt, we will be outgunned.'
structure32 = 'The border outpost reports a contingent of ' + str(random.randint(2,20)) + ' ' + secondary_actor + ' ' + transports + ' within sensor range. We should try to maintain diplomatic relations.'

structure33 = 'Captain\'s Log, Stardate ' + stardate + '. We are cautiously entering the ' + string.capwords(system_name) + ' star system, ' + str(random.randint(2,20)) + ' days after receiving a distress call from '+ regime + ' colony. The garbled transmission reported the colony under attack.'
structure34 = 'Captain\'s log, Stardate ' + stardate + '. Admiral ' + names.get_first_name() + ' and Lieutenant Commander ' + names.get_first_name() + ' of Starfleet Tactical have arrived to review the disappearance of New ' + bruteForceRandomWord('noun', 10).title() + ' colony. No sign remains of the ' + str(random.randint(100,1000)) + ' inhabitants.'

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

structure55 = 'In a shocking finding, scientists have discovered a ' + group + ' ' + secondary_actors + ' living in a previously unexplored ' + random.choice(physical_space) + '. Even more surprising to the researchers is the fact that the ' + secondary_actors + ' appear to be both ' + primary_actor_desc + ' and ' + secondary_actor_desc + '.'
print(structure55)
print(len(structure55))
quit()



tweets = []
tweets.extend([structure1, structure2, structure3, structure4, structure5, structure7, structure8, structure9, structure10, structure11, structure12, structure13, structure14, structure15, structure16, structure17, structure18, structure19, structure20, structure21, structure22, structure23, structure24, structure25, structure26, structure27, structure28, structure29, structure30, structure31, structure32, structure33, structure34, structure35, structure36, structure37, structure38, structure39, structure40, structure41, structure42, structure43, structure44, structure45, structure46, structure47, structure48, structure49, structure50, structure51, structure52, structure53, structure54])

under280 = []
for i in tweets:
    if len(i) <= 280:
        under280.append(i)


response = requests.get("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"quote\"]{quote,author->{author},source->{source}}")
DictA = response.json()

sentences = []
for result in DictA['result']:
    author = result['author']['author']
    quote = result['quote']
    source = result['source']['source']
    sentence = quote + ' ~ ' + author + ', ' + source
    sentences.append(sentence)


tweet_sentence = random.choice(under280)
print(tweet_sentence)
quit()

tweet_quote = random.choice(sentences)
print(tweet_quote)

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