from sentences.base_sentence import base_sentence

class sentence53(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'In a shocking finding, scientists have discovered a '
        sentence += components['group'] 
        sentence += ' ' + components['secondary_actors'] 
        sentence += ' living in a previously unexplored ' + components['physical_space']
        sentence += '. Even more surprising to the researchers is the fact that the '
        sentence += components['secondary_actors']
        sentence += ' appear to be both ' + components['primary_actor_desc']
        sentence += ' and ' + components['secondary_actor_desc']
        sentence += '.'

        return sentence
