from sentences.base_sentence import base_sentence
import random
import string

class sentence33(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Captain\'s Log, Stardate ' + components['stardate']
        sentence += '. We are cautiously entering the ' + string.capwords(components['system_name'])
        sentence += ' star system, ' + str(random.randint(2,20))
        sentence += ' days after receiving a distress call from ' + components['regime']
        sentence += ' colony. The garbled transmission reported the colony under attack.'

        return sentence
