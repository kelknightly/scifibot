from sentences.base_sentence import base_sentence

class sentence51(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'We\'re taking a short detour to explore a port with a neutral market. Apparently you can get anything there. We hope to get a good deal on '
        sentence += components['transport_equipped'] 
        sentence += ' for our ' + components['transport'] 
        sentence += '.'

        return sentence
