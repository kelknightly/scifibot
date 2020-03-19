from sentences.base_sentence import base_sentence

class sentence46(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['transport_article_on_desc'].title()
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' looms in the distant blackness of space. Its ' + components['engine']
        sentence += ' flares, and the ' + components['secondary_actors']
        sentence += ' onboard prepare for battle.'

        return sentence
