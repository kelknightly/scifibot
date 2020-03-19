from sentences.base_sentence import base_sentence

class sentence4(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article_on_desc'].title() 
        sentence += ' ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' ' + components['sentient_action'] 
        sentence += ' ' + components['secondary_actor_article_on_desc'] 
        sentence += ' ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actor']
        sentence += ' ' + components['place_prep']
        sentence += ' ' + components['place_article_on_desc']
        sentence += ' ' + components['place_desc']
        sentence += ' ' + components['place']
        sentence += '.'

        return sentence
