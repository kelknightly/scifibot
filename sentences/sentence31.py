from sentences.base_sentence import base_sentence
import random

class sentence31(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'The border outpost reports a contingent of ' + str(random.randint(2,20))
        sentence += ' ' + components['secondary_actor']
        sentence += ' ' + components['transports'] 
        sentence += ' within sensor range. ' + components['in-range']

        return sentence
