from sentences.base_sentence import base_sentence

class sentence18(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Several ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actors'] 
        sentence += ' drift in empty space'
        sentence += components['drifting_consequence'] 

        return sentence
