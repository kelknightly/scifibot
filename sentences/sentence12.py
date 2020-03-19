from sentences.base_sentence import base_sentence

class sentence12(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'You have stumbled upon ' + components['transport_article_on_desc']
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' from ' + components['regime'] 
        sentence += '. It is equipped with ' + components['transport_equipped'] 
        sentence += ' and ' + components['transport_equipped2'] 
        sentence += '.'

        return sentence
