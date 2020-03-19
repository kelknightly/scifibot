from sentences.base_sentence import base_sentence
import names
from sentences.sentence_generator import sentence_generator
import random

class sentence34(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Captain\'s Log, Stardate ' + components['stardate']
        sentence += '. Admiral ' + names.get_first_name()
        sentence += ' and Lieutenant Commander ' + names.get_first_name()
        sentence += ' of Starfleet Tactical have arrived to review the disappearance of the New ' + sentence_generator.get_random_word(self, 'noun', 10).title()
        sentence += ' colony. No sign remains of the ' + str(random.randint(100,1000))
        sentence += ' inhabitants.'

        return sentence