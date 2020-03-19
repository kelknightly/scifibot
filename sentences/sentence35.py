from sentences.base_sentence import base_sentence
import names
from sentences.sentence_generator import sentence_generator
import random

class sentence35(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Captain\'s Log, Stardate ' + components['stardate']
        sentence += '. We\'ve been ordered to Starbase ' + str(random.randint(10,90))
        sentence += ' in orbit around ' + sentence_generator.get_random_word(self, 'noun', 10).title()
        sentence += ' ' + components['roman_numeral'] 
        sentence += '. The ' + components['weapon_desc']
        sentence += ' ' + components['weapon']
        sentence += ' has been glitching and needs an urgent upgrade before another crewmember dies.'

        return sentence