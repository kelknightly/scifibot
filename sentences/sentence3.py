from sentences.base_sentence import base_sentence

class sentence3(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article_on_desc'].title() 
        sentence += ' ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' with ' + components['weapon_article_on_desc'] 
        sentence += ' ' + components['weapon_desc'] 
        sentence += ' ' + components['weapon'] 
        sentence += ' ' + components['sentient_negative_action']
        sentence += ' ' + components['secondary_actor_article_on_desc']
        sentence += ' ' + components['secondary_actor_desc']
        sentence += ' ' + components['secondary_actor']
        sentence += '.'

        return sentence
