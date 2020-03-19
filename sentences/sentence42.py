from sentences.base_sentence import base_sentence
import string

class sentence42(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'You are the Commander of ' + components['transport_article_on_desc']
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' and have decided to name it \'' + string.capwords(components['transport_name_desc'])
        sentence += ' ' + string.capwords(components['transport_name_noun'])
        sentence += '\'. It has a dual function: ' + components['transport_function']
        sentence += ', and ' + components['transport_function2']
        sentence += '.'

        return sentence
