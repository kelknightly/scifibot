from sentences.base_sentence import base_sentence

class sentence50(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['transport_article_on_desc'].title()
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' orbits ' + components['place_article_on_desc']
        sentence += ' ' + components['place_desc'] 
        sentence += ' ' + components['place']
        sentence += '. Its ' + components['secondary_actor_desc']
        sentence += ' inhabitants have tamed a ' + components['group']
        sentence += ' ' + components['secondary_actor_desc2']
        sentence += ' ' + components['secondary_actors']
        sentence += '.'

        return sentence
