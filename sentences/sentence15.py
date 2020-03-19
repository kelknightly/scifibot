from sentences.base_sentence import base_sentence
from sentences.sentence_generator import sentence_generator
import random

class sentence15(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article_on_desc'].title() 
        sentence += ' ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' manoeuvres ' + components['transport_article'] 
        sentence += ' ' + components['transport'] 
        sentence += '. ' + components['pronoun'].title()
        sentence += '\'s been hired to protect ' + components['planetsystemsector']
        sentence += ' ' + sentence_generator.get_random_word(self, 'noun', 10).title()+str(random.randint(100,999))
        sentence += ' from invaders.'

        return sentence