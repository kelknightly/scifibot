from sentences.base_sentence import base_sentence

class sentence8(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['actor_article_on_desc'].title() 
        sentence += ' ' + components['actor_desc'] 
        sentence += ' ' + components['actor'] 
        sentence += ' ' + components['place_action'] 
        sentence += ' ' + components['place_article_on_desc'] 
        sentence += ' ' + components['place_desc'] 
        sentence += ' ' + components['place'] 
        sentence += '. ' + components['history']

        return sentence
