from sentences.base_sentence import base_sentence

class sentence28(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'I was ' + components['sentient_action_plural']
        sentence += ' ' + components['secondary_actor_article_on_desc'] 
        sentence += ' ' + components['secondary_actor_desc'] 
        sentence += ' ' + components['secondary_actor'] 
        sentence += ' the day the ' + components['secondary_actors']
        sentence += ' attacked.'

        return sentence
