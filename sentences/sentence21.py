from sentences.base_sentence import base_sentence

class sentence21(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Several ' + components['secondary_actor_desc'].title() 
        sentence += ' ' + components['secondary_actors'] 
        sentence += ' drift in empty space, much too far to be rescued. They are alone.'

        return sentence
