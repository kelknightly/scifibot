from sentences.base_sentence import base_sentence

class sentence17(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['place_article_on_desc'].title() 
        sentence += ' ' + components['place_desc'] 
        sentence += ' ' + components['place'] 
        sentence += ' flies through space driven by ' + components['engine_article'] 
        sentence += ' ' + components['engine'] 
        sentence += '.'

        return sentence

