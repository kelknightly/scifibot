import requests
import json
import random
import time
import string
import names

# sentence generator class has a list of sentences (sentence objects)
# and list of sentence components

class sentence_generator:
    components = {}
    sentences = []

    def __init__(self):
        self.sentences = []

    def add_sentence(self, sentence):
        self.sentences.append(sentence)

    def print_all_sentences(self):
        for sentence in self.sentences:
            sentence_string = sentence.get_sentence(self.components)
            print(sentence.get_name() + ': ' + sentence_string) 

    def print_sentence_by_name(self, sentence_name):
        for sentence in self.sentences:
            if sentence_name == sentence.get_name():
                sentence_string = sentence.get_sentence(self.components)
                print(sentence.get_name() + ': ' + sentence_string)

    def get_all_sentences(self, max_length):
        eligible_sentences = []
        for sentence in self.sentences:
            sentence_string = sentence.get_sentence(self.components)
            if len(sentence_string) <= max_length:
                eligible_sentences.append(sentence_string)

        return eligible_sentences
             
    def populate_components(self):
        nouns = self.get_noun_list("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"noun\"]{noun,nounType->{nounType}}")
        descriptions = self.get_description_list("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"description\"]{description,nounType->{nounType}}")
        actions = self.get_action_list("https://3hjj9iij.api.sanity.io/v1/data/query/production?query=*[_type==\"action\"]{action,actionType->{actionType}}")

        # Getting lists of Nouns
        self.components['list_primary_actor'] = self.get_noun_list_for_type(nouns, 'primary actor')
        self.components['list_secondary_actor'] = self.get_noun_list_for_type(nouns, 'secondary actor')
        self.components['list_actor'] = self.components['list_primary_actor'] + self.components['list_secondary_actor']
        self.components['list_in_place'] = self.get_noun_list_for_type(nouns, 'in-place')
        self.components['list_on_place'] = self.get_noun_list_for_type(nouns, 'on-place')
        self.components['list_place'] = self.components['list_in_place'] + self.components['list_on_place']
        self.components['list_weapon'] = self.get_noun_list_for_type(nouns, 'weapon')
        self.components['list_transport'] = self.get_noun_list_for_type(nouns, 'transport')
        self.components['list_transport_damage_noun'] = self.get_noun_list_for_type(nouns, 'transport damage')
        self.components['list_regime'] = self.get_noun_list_for_type(nouns, 'politics')
        self.components['list_group'] = self.get_noun_list_for_type(nouns, 'group')
        self.components['list_secondary_actor_plural'] = self.get_noun_list_for_type(nouns, 'secondary actors plural')
        self.components['list_measuring_things'] = self.get_noun_list_for_type(nouns, 'measuring')
        self.components['list_liquid'] = self.get_noun_list_for_type(nouns, 'liquid')
        self.components['list_tech'] = self.get_noun_list_for_type(nouns, 'tech')
        self.components['list_transport_name'] = self.get_noun_list_for_type(nouns, 'transport name')
        self.components['list_transports'] = self.get_noun_list_for_type(nouns, 'transport plural')
        self.components['list_engine'] = self.get_noun_list_for_type(nouns, 'engine')

        # Getting lists of Descriptions
        self.components['list_in_place_description'] = self.get_description_list_for_type(descriptions, 'in-place')
        self.components['list_on_place_description'] = self.get_description_list_for_type(descriptions, 'on-place')
        self.components['list_place_description'] = self.components['list_in_place_description'] + self.components['list_on_place_description']
        self.components['list_primary_actor_description'] = self.get_description_list_for_type(descriptions, 'primary actor')
        self.components['list_secondary_actor_description'] = self.get_description_list_for_type(descriptions, 'secondary actor')
        self.components['list_actor_description'] = self.components['list_primary_actor_description'] + self.components['list_secondary_actor_description']
        self.components['list_weapon_description'] = self.get_description_list_for_type(descriptions, 'weapon')
        self.components['list_transport_description'] = self.get_description_list_for_type(descriptions, 'transport')
        self.components['list_transport_equipped'] = self.get_description_list_for_type(descriptions, 'transport equipped')
        self.components['list_a__society'] = self.get_description_list_for_type(descriptions, 'a__society')
        self.components['list_liquid_desc'] = self.get_description_list_for_type(descriptions, 'liquid')
        self.components['list_society_is_a__'] = self.get_description_list_for_type(descriptions, 'society_is_a__')
        self.components['list_crust'] = self.get_description_list_for_type(descriptions, 'crust')
        self.components['list_sky'] = self.get_description_list_for_type(descriptions, 'sky')
        self.components['list_transport_name_desc'] = self.get_description_list_for_type(descriptions, 'transport name')

        # Getting lists of Actions
        self.components['list_place_action'] = self.get_action_list_for_type(actions, 'place')
        self.components['list_weapon_action'] = self.get_action_list_for_type(actions, 'weapon')
        self.components['list_transport_action'] = self.get_action_list_for_type(actions, 'transport')
        self.components['list_sentient_positive_action'] = self.get_action_list_for_type(actions, 'sentient positive')
        self.components['list_sentient_negative_action'] = self.get_action_list_for_type(actions, 'sentient negative')
        self.components['list_sentient_action'] = self.components['list_sentient_positive_action'] + self.components['list_sentient_negative_action']
        self.components['list_transport_function'] = self.get_action_list_for_type(actions, 'transport function')
        self.components['list_transport_damage_action'] = self.get_action_list_for_type(actions, 'transport damage')
        self.components['list_suddenly'] = self.get_action_list_for_type(actions, 'suddenly')
        self.components['list_sentient_action_plural'] = self.get_action_list_for_type(actions, 'sentient plural')
        self.components['list_transport_about'] = self.get_action_list_for_type(actions, 'transport about')
        self.components['list_looking_for'] = self.get_action_list_for_type(actions, 'looking for')

        # Randomly selecting a word within each list
        self.components['in_place'] = random.choice(self.components['list_in_place'])
        self.components['on_place'] = random.choice(self.components['list_on_place'])
        self.components['place'] = random.choice(self.components['list_place'])
        self.components['place_action'] = random.choice(self.components['list_place_action'])
        self.components['place_desc'] = random.choice(self.components['list_place_description'])
        self.components['secondary_actor'] = random.choice(self.components['list_secondary_actor'])
        self.components['primary_actor'] = random.choice(self.components['list_primary_actor'])
        self.components['weapon_action'] = random.choice(self.components['list_weapon_action'])
        self.components['transport_action'] = random.choice(self.components['list_transport_action'])
        self.components['sentient_positive_action'] = random.choice(self.components['list_sentient_positive_action'])
        self.components['sentient_negative_action'] = random.choice(self.components['list_sentient_negative_action'])
        self.components['sentient_action'] = random.choice(self.components['list_sentient_action'])
        self.components['primary_actor_desc'] = random.choice(self.components['list_primary_actor_description'])
        self.components['secondary_actor_desc'] = random.choice(self.components['list_secondary_actor_description'])
        self.components['weapon_desc'] = random.choice(self.components['list_weapon_description'])
        self.components['transport_desc'] = random.choice(self.components['list_transport_description'])
        self.components['weapon'] = random.choice(self.components['list_weapon'])
        self.components['transport'] = random.choice(self.components['list_transport'])
        self.components['actor'] = random.choice(self.components['list_actor'])
        self.components['actor_desc'] = random.choice(self.components['list_actor_description'])
        self.components['transport_function'] = random.choice(self.components['list_transport_function'])
        self.components['transport_damage_action'] = random.choice(self.components['list_transport_damage_action'])
        self.components['transport_equipped'] = random.choice(self.components['list_transport_equipped'])
        self.components['transport_damage_noun'] = random.choice(self.components['list_transport_damage_noun'])
        self.components['regime'] = random.choice(self.components['list_regime'])
        self.components['group'] = random.choice(self.components['list_group'])
        self.components['a__society'] = random.choice(self.components['list_a__society'])
        self.components['secondary_actors'] = random.choice(self.components['list_secondary_actor_plural'])
        self.components['measuring_things'] = random.choice(self.components['list_measuring_things'])
        self.components['suddenly'] = random.choice(self.components['list_suddenly'])
        self.components['liquid'] = random.choice(self.components['list_liquid'])
        self.components['liquid_desc'] = random.choice(self.components['list_liquid_desc'])
        self.components['sentient_action_plural'] = random.choice(self.components['list_sentient_action_plural'])
        self.components['society_is_a__'] = random.choice(self.components['list_society_is_a__'])
        self.components['tech'] = random.choice(self.components['list_tech'])
        self.components['crust'] = random.choice(self.components['list_crust'])
        self.components['sky'] = random.choice(self.components['list_sky'])
        self.components['transport_name_noun'] = random.choice(self.components['list_transport_name'])
        self.components['transport_name_desc'] = random.choice(self.components['list_transport_name_desc'])
        self.components['transport_about'] = random.choice(self.components['list_transport_about'])
        self.components['transports'] = random.choice(self.components['list_transports'])
        self.components['engine'] = random.choice(self.components['list_engine'])
        self.components['looking_for'] = random.choice(self.components['list_looking_for'])

        # Randomising a second time for variables that are used twice in a sentence
        self.components['place2'] = random.choice(self.components['list_place'])
        self.components['place2_desc'] = random.choice(self.components['list_place_description'])
        self.components['secondary_actor2'] = random.choice(self.components['list_secondary_actor'])
        self.components['transport_equipped2'] = random.choice(self.components['list_transport_equipped'])
        self.components['transport_function2'] = random.choice(self.components['list_transport_function'])
        self.components['secondary_actor_desc2'] = random.choice(self.components['list_secondary_actor_description'])
        self.components['primary_actor2'] = random.choice(self.components['list_primary_actor'])

        self.components['place2'] = self.randomiser_duplicator(self.components['place'], self.components['place2'], self.components['list_place'])
        self.components['place2_desc'] = self.randomiser_duplicator(self.components['place_desc'], self.components['place2_desc'], self.components['list_place_description'])
        self.components['secondary_actor2'] = self.randomiser_duplicator(self.components['secondary_actor'], self.components['secondary_actor2'], self.components['list_secondary_actor'])
        self.components['transport_function2'] = self.randomiser_duplicator(self.components['transport_function'], self.components['transport_function2'], self.components['list_transport_function'])
        self.components['secondary_actor_desc2'] = self.randomiser_duplicator(self.components['secondary_actor_desc'], self.components['secondary_actor_desc2'], self.components['list_secondary_actor_description'])
        self.components['primary_actor2'] = self.randomiser_duplicator(self.components['primary_actor'], self.components['primary_actor2'], self.components['list_primary_actor'])

        self.components['primary_actor_article_on_desc'] = self.article(self.components['primary_actor_desc'])
        self.components['secondary_actor_article_on_desc'] = self.article(self.components['secondary_actor_desc'])
        self.components['place_article_on_desc'] = self.article(self.components['place_desc'])
        self.components['weapon_article_on_desc'] = self.article(self.components['weapon_desc'])
        self.components['transport_article_on_desc'] = self.article(self.components['transport_desc'])
        self.components['actor_article_on_desc'] = self.article(self.components['actor_desc'])
        self.components['primary_actor_article'] = self.article(self.components['primary_actor'])
        self.components['secondary_actor_article'] = self.article(self.components['secondary_actor'])
        self.components['place_article'] = self.article(self.components['place'])
        self.components['weapon_article'] = self.article(self.components['weapon'])
        self.components['transport_article'] = self.article(self.components['transport'])
        self.components['actor_article'] = self.article(self.components['actor'])
        self.components['a__society_article'] = self.article(self.components['a__society'])
        self.components['secondary_actor2_article'] = self.article(self.components['secondary_actor2'])
        self.components['place2_article'] = self.article(self.components['place2'])
        self.components['primary_actor2_article'] = self.article(self.components['primary_actor2'])
        self.components['place2_article_on_desc'] = self.article(self.components['place2_desc'])
        self.components['society_is_a__article'] = self.article(self.components['society_is_a__'])
        self.components['crust_article'] = self.article(self.components['crust'])
        self.components['engine_article'] = self.article(self.components['engine'])

        # Listing prepositions
        self.components['list_weapon_preposition'] = ['with', 'using']
        self.components['weapon_preposition'] = random.choice(self.components['list_weapon_preposition'])
        self.components['list_transport_preposition'] = ['aboard', 'on']
        self.components['transport_preposition'] = random.choice(self.components['list_transport_preposition'])

        if self.components['place'] in self.components['list_in_place']:
            self.components['place_prep'] = 'in'
        if self.components['place'] in self.components['list_on_place']:
            self.components['place_prep'] = 'on'

        self.components['list_pronoun'] = ['she', 'he']
        self.components['pronoun'] = random.choice(self.components['list_pronoun'])
        
        # possessive pronoun
        if self.components['pronoun'] == 'she':
            self.components['pos_pro'] = 'her'
        if self.components['pronoun'] == 'he':
            self.components['pos_pro'] = 'his'

        self.components['list_planetsystemsector'] = ['Planet', 'System', 'Sector']
        self.components['planetsystemsector'] = random.choice(self.components['list_planetsystemsector'])

        self.components['measuring'] = ['measuring', 'considering', 'tracking']
        self.components['measuring'] = random.choice(self.components['measuring'])
                
        self.components['verb'] = self.get_random_word('verb', 10)
        self.components['noun1'] = self.get_random_word('noun', 10)
        self.components['noun2'] = self.get_random_word('noun', 10)
        self.components['name'] = self.components['verb'].title() + ' ' + self.components['noun1'].title() + ' the ' + self.components['noun2'].title()
    
        if self.components['place'] == 'civilisation':
            self.components['civ_soc'] = 'society'
        else:
            self.components['civ_soc'] = 'civilisation'

        self.components['list_alpha'] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.components['liquid_type'] = random.choice(['it rains', 'there are deep oceans of', 'there are clouds of', 'there are pools of', 'rivers run with', 'the skies are full of', 'there is an ocean of'])

        self.components['stardate'] = str(random.randint(1000, 56947)) + '.' + str(random.randint(1,9))
        self.components['system_name'] = self.get_random_word('noun', 5) + ' ' + self.get_random_word('noun', 5)

        self.components['roman_numeral'] = random.choice(['I','II','III','IV','V','VI','VII','VIII','X'])

        self.components['physical_space'] = random.choice(['valley', 'cavern', 'cave', 'crevasse'])

        self.components['person_title'] = random.choice(['Ms', 'Mr', 'Dr'])

    # Function to place 'a' or 'an' before a noun
    def article(self, i):
        if i[0] in ('a','e','i','o','u','A','E','I','O','U'):
            article = 'an'
        elif i in ('useless','euphoric','euphemism','usurper','eunuch','eulogy','upsilon meson','eugenist','Ukrainian','utilitarian'):
            article = 'a'
        else: 
            article = 'a'
        return article
    
    def randomiser_duplicator(self, val1, val2, val_list):
        while val1 == val2:
            val2 = random.choice(val_list)
            if val1 != val2:
                return val2
        return val2

    def get_noun_list(self, query):
        response = requests.get(query)
        DictA = response.json()
        nouns = []
        for result in DictA['result']:
            nouns.append({
                "noun": result['noun'],
                "type": result['nounType']['nounType']
            })
        return(nouns)

    def get_noun_list_for_type(self, nouns, nounType_filter):
        noun_list = []
        for noun in nouns:
            if noun['type'] == nounType_filter:
                noun_list.append(noun['noun'])
        return noun_list


    def get_description_list(self, query):
        response = requests.get(query)
        DictA = response.json()
        descriptions = []
        for result in DictA['result']:
            descriptions.append({
                "description": result['description'],
                "type": result['nounType']['nounType']
            })
        return(descriptions)

    def get_description_list_for_type(self, descriptions, nounType_filter):
        description_list = []
        for description in descriptions:
            if description['type'] == nounType_filter:
                description_list.append(description['description'])
        return description_list


    def get_action_list(self, query):
        response = requests.get(query)
        DictA = response.json()
        actions = []
        for result in DictA['result']:
            actions.append({
                "action": result['action'],
                "type": result['actionType']['actionType']
            })
        return(actions)

    def get_action_list_for_type(self, actions, actionType_filter):
        action_list = []
        for action in actions:
            if action['type'] == actionType_filter:
                action_list.append(action['action'])
        return action_list

    def get_random_word(self, part, length):
        url = "https://wordsapiv1.p.rapidapi.com/words/"
        querystring = {"random":"true"}
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': "d13b08e2c9mshdb21833bede88e1p13c577jsn79fe44d0a6f9"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        js = response.json()
        return js['word']