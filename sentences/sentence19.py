from sentences.base_sentence import base_sentence
import random

class sentence19(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'Your crew has stranded you on ' + components['a__planet_article']
        sentence += ' ' + components['a__planet'] + ' planet named '
        sentence += components['planetname'] + ' with no spare water or oxygen. '
        sentence += components['stranded']

        return sentence
