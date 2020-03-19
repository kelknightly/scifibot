from sentences.base_sentence import base_sentence

class sentence24(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['regime'].title() 
        sentence += ' has tasked you with tracking, capturing, and returning ' + components['secondary_actor_article_on_desc'] 
        sentence += ' ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actor']
        sentence += ' lost ' + components['place_prep'] 
        sentence += ' a distant ' + components['place'] 
        sentence += '. It will take all your skills as ' + components['primary_actor_article']
        sentence += ' ' + components['primary_actor']
        sentence += '.'

        return sentence