from sentences.base_sentence import base_sentence

class sentence19(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Several ' + components['secondary_actor_desc'].title() 
        sentence += ' ' + components['secondary_actors'] 
        sentence += ' drift in empty space. They screwed the pooch on this one.'

        return sentence
