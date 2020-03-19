from sentences.base_sentence import base_sentence

class sentence14(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'You are the Captain of ' + components['transport_article_on_desc']
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' from ' + components['regime'] 
        sentence += '. It has a dual function: ' + components['transport_function'] 
        sentence += ', and ' + components['transport_function2'] 
        sentence += '.'

        return sentence
