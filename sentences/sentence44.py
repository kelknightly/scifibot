from sentences.base_sentence import base_sentence

class sentence44(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['a__society_article'].title()
        sentence += ' ' + components['a__society'] 
        sentence += ' ' + components['civ_soc'] 
        sentence += ' is involved in the business of relocating ' + components['place_article_on_desc']
        sentence += ' ' + components['place_desc']
        sentence += ' ' + components['place']
        sentence += ' using ' + components['engine_article']
        sentence += ' ' + components['engine']
        sentence += '.'

        return sentence
