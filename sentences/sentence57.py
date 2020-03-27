from sentences.base_sentence import base_sentence

class sentence57(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'The ' + components['primary_actor_desc'] 
        sentence += ' ' + components['primary_actor'] 
        sentence += ' runs for ' + components['pos_pro'] + ' life. '
        sentence += components['secondary_actor_article'].title()
        sentence += ' ' + components['secondary_actor'] 
        sentence += ' pursues ' + components['obj_pro']
        sentence+= ' with single-minded determination. It will retrieve its ' 
        sentence += components['basic_noun']
        sentence += ', whatever the cost.'

        return sentence
