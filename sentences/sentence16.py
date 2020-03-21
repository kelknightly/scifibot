from sentences.base_sentence import base_sentence

class sentence16(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article_on_desc'].title() 
        sentence += ' ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' drifts helplessly in empty space. ' + components['pos_pro'].title()
        sentence += ' ' + components['transport'] 
        sentence += ' has been damaged by ' + components['transport_damage_noun'] 
        sentence += ' and ' + components['pronoun'] 
        sentence += ' needs immediate assistance.'

        return sentence
