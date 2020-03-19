from sentences.base_sentence import base_sentence
import random

class sentence38(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'NASA has discovered an inhabited exoplanet. The society appears to be '
        sentence += components['society_is_a__article'] 
        sentence += ' ' + components['society_is_a__']
        sentence += ', and early scans reveal advanced ' + components['tech']
        sentence += ' and ' + components['crust_article']
        sentence += ' ' + components['crust']
        sentence += ' crust. The sky is ' + components['sky']
        sentence += ' and a day lasts ' + str(random.randint(2,100))
        sentence += ' Earth hours.'

        return sentence
