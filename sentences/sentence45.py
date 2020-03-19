from sentences.base_sentence import base_sentence

class sentence45(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'You have stumbled upon ' + components['transport_article_on_desc']
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' from ' + components['regime']
        sentence += '. It is equipped with ' + components['transport_equipped']
        sentence += ' and boasts ' + components['engine_article']
        sentence += ' ' + components['engine']
        sentence += '.'

        return sentence
