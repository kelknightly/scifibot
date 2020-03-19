from sentences.base_sentence import base_sentence

class sentence49(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article_on_desc'].title()
        sentence += ' ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' drifts helplessly in space. ' + components['pronoun'].title()
        sentence += ' is unconscious, and ' + components['pos_pro'] 
        sentence += ' ' + components['transport']
        sentence += ' is ' + components['transport_damage_action']
        sentence += '.'

        return sentence
