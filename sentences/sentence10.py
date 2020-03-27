from sentences.base_sentence import base_sentence

class sentence10(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['place_article_on_desc'].title() 
        sentence += ' ' + components['place_desc'] 
        sentence += ' ' + components['place'] 
        sentence += ' orbits ' + components['place2_article'] 
        sentence += ' ' + components['place2'] 
        sentence += '. It is home to a ' + components['group'] 
        sentence += ' ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actors']
        sentence += ' ' + components['looking_for']
        sentence += '.'

        return sentence