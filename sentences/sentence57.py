from sentences.base_sentence import base_sentence

class sentence57(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'The ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' ran for ' + components['pos_pro'] + ' life. '
        sentence += components['secondary_actor_article'].title()
        sentence += ' ' + components['secondary_actor'] 
        sentence += ' pursued ' + components['obj_pro']
        sentence+= ' with single-minded determination. It would retrieve its ' 
        sentence += components['silly_noun1']
        sentence += ', whatever the cost.'

        return sentence
