from sentences.base_sentence import base_sentence

class sentence39(base_sentence):
    
    def get_sentence(self, components):
        sentence = '\"Oh God, they\'re breaking through!\" '
        sentence += components['person_title'] + ' ' + components['silly_name1'][1].title() 
        sentence += ' screamed. \"They\'re nearly through ' 
        sentence += components['breaking_through'] + '! They\'re using '
        sentence += components['silly_thing'] + ' to get in!\"'

        return sentence
