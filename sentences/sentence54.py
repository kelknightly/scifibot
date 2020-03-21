from sentences.base_sentence import base_sentence

class sentence54(base_sentence):
    
    def get_sentence(self, components):
        sentence = components['primary_actor_article_on_desc'].title() 
        sentence += ' ' + components['primary_actor_desc']
        sentence += ' ' + components['primary_actor'] 
        sentence += ' is awaiting execution in ' + components['transport_article_on_desc']
        sentence += ' ' + components['transport_desc']
        sentence += ' ' + components['transport'] + '. '
        sentence += components['pos_pro'].title() + ' planet was destroyed by '
        sentence += components['secondary_actor_article_on_desc']
        sentence += ' ' + components['secondary_actor_desc']
        sentence += ' ' + components['secondary_actor']
        sentence += ' and ' + components['pronoun'] + ' is a prisoner of war.'

        return sentence