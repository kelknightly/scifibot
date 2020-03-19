from sentences.base_sentence import base_sentence
import string

class sentence40(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'You encounter '
        sentence += components['transport_article_on_desc'] 
        sentence += ' ' + components['transport_desc']
        sentence += ' ' + components['transport']
        sentence += ' with the words \'' + string.capwords(components['transport_name_desc'])
        sentence += ' ' + string.capwords(components['transport_name_noun'])
        sentence += '\' painted on the side. It ' + components['transport_about']
        sentence += ' and is equipped with ' + components['transport_equipped']
        sentence += '.'

        return sentence
