from sentences.base_sentence import base_sentence

# Child class of base_sentence class
# Inherits all functionality of the parent class
class sentence1(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article_on_desc'].title() 
        sentence += ' ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' named \'' 
        sentence += components['name'] 
        sentence += '\' ' + components['sentient_action'] 
        sentence += ' ' + components['secondary_actor_article_on_desc']  
        sentence += ' ' 
        sentence += components['secondary_actor_desc'] 
        sentence += ' ' 
        sentence += components['secondary_actor'] 
        sentence += '.'
        
        return sentence