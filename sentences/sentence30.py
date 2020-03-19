from sentences.base_sentence import base_sentence
import string
from sentences.sentence_generator import sentence_generator

class sentence30(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Belay my previous order, ' + components['person_title']
        sentence += ' ' + string.capwords(sentence_generator.get_random_word(self, 'noun', 10))
        sentence += '. We need a vital show of force. Activate the ' + components['weapon_desc'] 
        sentence += ' ' + components['weapon'] 
        sentence += ' and aim it at the ' + components['place'] 
        sentence += '.'

        return sentence
