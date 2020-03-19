from sentences.base_sentence import base_sentence

class sentence2(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article_on_desc'].title() 
        sentence += ' ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' ' + components['sentient_negative_action'] 
        sentence += ' ' + components['secondary_actor_article_on_desc'] 
        sentence += ' ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actor']
        sentence += ' ' + components['transport_preposition']
        sentence += ' ' + components['transport_article_on_desc']
        sentence += ' ' + components['transport_desc']
        sentence += ' ' + components['transport']
        sentence += '.'

        return sentence