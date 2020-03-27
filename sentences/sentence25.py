from sentences.base_sentence import base_sentence

class sentence25(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['secondary_actor_article_on_desc'].title() 
        sentence += ' ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actor'] 
        sentence += ' orbits ' + components['place_article_on_desc']
        sentence += ' ' + components['place_desc'] 
        sentence += ' ' + components['place'] 
        sentence += ', ' + components['orbits_verb']
        sentence += ' ' + components['orbits_noun'] + '.'

        return sentence