from sentences.base_sentence import base_sentence
import silly

class sentence59(base_sentence):
    
    def get_sentence(self, components):
        sentence = '\"Oh God, they\'re breaking through!\" '
        sentence += components['person_title'] + ' ' + components['silly_name1'][1].title() 
        sentence += ' screamed. \"They\'re nearly through ' 
        sentence += components['breaking_through'] + '! They\'re using '
        sentence += silly.a_thing() + ' to get in!\"'

        return sentence
