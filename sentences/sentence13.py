from sentences.base_sentence import base_sentence

class sentence13(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'You have stumbled upon ' + components['transport_article_on_desc']
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' from ' + components['regime'] 
        sentence += '. With ' + components['engine_article'] 
        sentence += ' ' + components['engine'] 
        sentence += ', it is one of the most powerful ships in the galaxy.'

        return sentence
