from sentences.base_sentence import base_sentence

class sentence58(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'The first planet discovery of the ' 
        sentence += components['rhyme_word1'].upper() + '-' + components['rhyme_word2'].title()
        sentence += ' Survey has been announced. ' + components['planet_name'] 
        sentence += ' is ' + components['silly_adjective1']
        sentence += ' and ' + components['silly_adjective2']
        sentence += ', and seems to be covered in '
        sentence += components['silly_plural1'] + '.'

        return sentence
