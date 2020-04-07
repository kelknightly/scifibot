from sentences.base_sentence import base_sentence

class sentence53(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'The lone survivor of a mysterious spaceship incident hasn\'t returned home alone - hiding inside '
        sentence += components['pos_pro']
        sentence += ' body is ' + components['secondary_actor_article_on_desc'] 
        sentence += ' ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actor'] + '.'

        return sentence
