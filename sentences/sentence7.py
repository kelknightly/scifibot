from sentences.base_sentence import base_sentence

class sentence7(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['secondary_actor_article_on_desc'].title() 
        sentence += ' ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actor'] 
        sentence += ' from ' + components['place_article_on_desc'] 
        sentence += ' ' + components['place_desc'] 
        sentence += ' ' + components['place'] 
        sentence += ' ' + components['weapon_action']
        sentence += ' ' + components['weapon_article_on_desc']
        sentence += ' ' + components['weapon_desc']
        sentence += ' ' + components['weapon']
        sentence += '.'

        return sentence
