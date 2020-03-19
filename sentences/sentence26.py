from sentences.base_sentence import base_sentence

class sentence26(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['transport_article_on_desc'].title() 
        sentence += ' ' + components['transport_desc'] 
        sentence += ' ' + components['transport'] 
        sentence += ' you assumed to be friendly suddenly ' + components['suddenly']
        sentence += '.'

        return sentence
