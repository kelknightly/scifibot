from sentences.base_sentence import base_sentence
import string

class sentence43(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'You are the Commander of ' + components['transport_article_on_desc']
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' and have decided to name it \'' + string.capwords(components['transport_name_desc'])
        sentence += ' ' + string.capwords(components['transport_name_noun'])
        sentence += '\'. It ' + components['transport_about']
        sentence += ' and is the pride of ' + components['regime']
        sentence += '.'

        return sentence
