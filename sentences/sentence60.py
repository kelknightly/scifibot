#In 2015, a group of biohackers successfully injected chemicals into a volunteer’s eye that  gave him temporary night vision.

from sentences.base_sentence import base_sentence

class sentence60(base_sentence):
    
    def get_sentence(self, components):
        sentence = 'In ' + components['random_year']
        sentence += ', a ' + components['group'] + ' of '
        sentence += components['secondary_actors']
        sentence += ' successfully injected ' + components['sense_noun2'] + ' into a captive '
        sentence += components['primary_actor'] + '\'s '
        sentence += components['body_part'] + ', accidentally giving ' + components['obj_pro'] + ' the ability to '
        sentence += components['sense'] + ' ' + components['sense_noun'] + '.'

        return sentence
