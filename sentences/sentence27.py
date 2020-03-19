from sentences.base_sentence import base_sentence
from sentences.sentence_generator import sentence_generator
import random

class sentence27(base_sentence):
    
    def get_sentence(self, components):
        sentence = str(random.randint(100,999))
        sentence += ' light years away on the planet ' + sentence_generator.get_random_word(self, 'noun', 10).upper() 
        sentence += '-' + str(random.randint(1,100)) + random.choice(components['list_alpha'])
        sentence += ', ' + components['liquid_type']
        sentence += ' ' + components['liquid_desc'] 
        sentence += ' ' + components['liquid'] 
        sentence += '.'

        return sentence