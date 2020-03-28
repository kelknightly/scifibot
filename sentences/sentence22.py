from sentences.base_sentence import base_sentence
import random
import string

class sentence22(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article'].title() 
        sentence += ' ' + components['primary_actor'] 
        sentence += ', codename ' + (''.join(random.choice(string.ascii_letters) for x in range(5)))
        sentence += ', has been hired to abduct or kill ' + components['primary_actor_article_on_desc'] 
        sentence += ' ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor2']
        sentence += ', but needs ' + components['weapon_article_on_desc']
        sentence += ' ' + components['weapon_desc']
        sentence += ' ' + components['weapon']
        sentence += ' to ' + components['hired_to']

        return sentence