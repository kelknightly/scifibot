from sentences.base_sentence import base_sentence

class sentence36(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['actor_article_on_desc'].title()
        sentence += ' ' + components['actor_desc'] 
        sentence += ' ' + components['actor']
        sentence += ' drifts in empty space, following the path of a particular ' + components['secondary_actor']
        sentence += ' through space-time.'

        return sentence
