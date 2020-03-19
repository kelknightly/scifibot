from sentences.base_sentence import base_sentence

class sentence11(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['place_article_on_desc'].title() 
        sentence += ' ' + components['place_desc'] 
        sentence += ' ' + components['place'] 
        sentence += ' is home to ' + components['a__society_article'] 
        sentence += ' ' + components['a__society'] 
        sentence += ' ' + components['civ_soc'] 
        sentence += ' of ' + components['secondary_actors']
        sentence += '. They have acquired ' + components['weapon_article_on_desc']
        sentence += ' ' + components['weapon_desc']
        sentence += ' ' + components['weapon']
        sentence += ' and will use it for war.'

        return sentence
