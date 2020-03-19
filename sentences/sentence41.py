from sentences.base_sentence import base_sentence

class sentence41(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'The ' + components['transport_desc']
        sentence += ' ' + components['transport'] 
        sentence += ' you\'ve encountered ' + components['transport_about'] 
        sentence += '. It seems to have a bad ' + components['secondary_actor']
        sentence += ' infestation, so probably best to steer clear of it.'

        return sentence
