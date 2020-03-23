from sentences.base_sentence import base_sentence

class sentence55(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Our next stop is a planet with ' + components['planet_with']
        sentence += ' and ' + components['planet_with2'] + '. '
        sentence += components['planet_end']

        return sentence
