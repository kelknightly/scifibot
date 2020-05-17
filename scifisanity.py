import requests
import json
import random
import time
import string
import names

# A central place where I can add everything once
# Let's me play with sentence structures independently
# Ties everything together
# 1 - instantiates a generator object
# 2 - makes sentences and push them into the generator

# Sentence construction
from sentences.sentence_generator import sentence_generator
from sentences.sentence1 import sentence1
from sentences.sentence2 import sentence2
from sentences.sentence3 import sentence3
from sentences.sentence4 import sentence4
from sentences.sentence5 import sentence5
from sentences.sentence6 import sentence6
from sentences.sentence7 import sentence7
from sentences.sentence8 import sentence8
from sentences.sentence9 import sentence9
from sentences.sentence10 import sentence10
from sentences.sentence11 import sentence11
from sentences.sentence12 import sentence12
from sentences.sentence13 import sentence13
from sentences.sentence14 import sentence14
from sentences.sentence15 import sentence15
from sentences.sentence16 import sentence16
from sentences.sentence17 import sentence17
#from sentences.sentence18 import sentence18
from sentences.sentence19 import sentence19
from sentences.sentence20 import sentence20
from sentences.sentence21 import sentence21
from sentences.sentence22 import sentence22
from sentences.sentence23 import sentence23
from sentences.sentence24 import sentence24
#from sentences.sentence25 import sentence25
from sentences.sentence26 import sentence26
from sentences.sentence27 import sentence27
from sentences.sentence28 import sentence28
from sentences.sentence29 import sentence29
from sentences.sentence30 import sentence30
from sentences.sentence31 import sentence31
from sentences.sentence32 import sentence32
from sentences.sentence33 import sentence33
from sentences.sentence34 import sentence34
from sentences.sentence35 import sentence35
from sentences.sentence36 import sentence36
from sentences.sentence37 import sentence37
from sentences.sentence38 import sentence38
from sentences.sentence39 import sentence39
from sentences.sentence40 import sentence40
from sentences.sentence41 import sentence41
from sentences.sentence42 import sentence42
from sentences.sentence43 import sentence43
from sentences.sentence44 import sentence44
from sentences.sentence45 import sentence45
from sentences.sentence46 import sentence46
from sentences.sentence47 import sentence47
from sentences.sentence48 import sentence48
from sentences.sentence49 import sentence49
from sentences.sentence50 import sentence50
from sentences.sentence51 import sentence51
from sentences.sentence52 import sentence52
from sentences.sentence53 import sentence53

class scifisanity(object):
    generator = None

    def __init__(self):
        self.generator = sentence_generator()
        self.generator.populate_components()

        self.generator.add_sentence(sentence1('Sentence 1'))
        self.generator.add_sentence(sentence2('Sentence 2'))
        self.generator.add_sentence(sentence3('Sentence 3'))
        self.generator.add_sentence(sentence4('Sentence 4'))
        self.generator.add_sentence(sentence5('Sentence 5'))
        self.generator.add_sentence(sentence6('Sentence 6'))
        self.generator.add_sentence(sentence7('Sentence 7'))
        self.generator.add_sentence(sentence8('Sentence 8'))
        self.generator.add_sentence(sentence9('Sentence 9'))
        self.generator.add_sentence(sentence10('Sentence 10'))
        self.generator.add_sentence(sentence11('Sentence 11'))
        self.generator.add_sentence(sentence12('Sentence 12'))
        self.generator.add_sentence(sentence13('Sentence 13'))
        self.generator.add_sentence(sentence14('Sentence 14'))
        self.generator.add_sentence(sentence15('Sentence 15'))
        self.generator.add_sentence(sentence16('Sentence 16'))
        self.generator.add_sentence(sentence17('Sentence 17'))
        #self.generator.add_sentence(sentence18('Sentence 18'))
        self.generator.add_sentence(sentence19('Sentence 19'))
        self.generator.add_sentence(sentence20('Sentence 20'))
        self.generator.add_sentence(sentence21('Sentence 21'))
        self.generator.add_sentence(sentence22('Sentence 22'))
        self.generator.add_sentence(sentence23('Sentence 23'))
        self.generator.add_sentence(sentence24('Sentence 24'))
        #self.generator.add_sentence(sentence25('Sentence 25'))
        self.generator.add_sentence(sentence26('Sentence 26'))
        self.generator.add_sentence(sentence27('Sentence 27'))
        self.generator.add_sentence(sentence28('Sentence 28'))
        self.generator.add_sentence(sentence29('Sentence 29'))
        self.generator.add_sentence(sentence30('Sentence 30'))
        self.generator.add_sentence(sentence31('Sentence 31'))
        self.generator.add_sentence(sentence32('Sentence 32'))
        self.generator.add_sentence(sentence33('Sentence 33'))
        self.generator.add_sentence(sentence34('Sentence 34'))
        self.generator.add_sentence(sentence35('Sentence 35'))
        self.generator.add_sentence(sentence36('Sentence 36'))
        self.generator.add_sentence(sentence37('Sentence 37'))
        self.generator.add_sentence(sentence38('Sentence 38'))
        self.generator.add_sentence(sentence39('Sentence 39'))
        self.generator.add_sentence(sentence40('Sentence 40'))
        self.generator.add_sentence(sentence41('Sentence 41'))
        self.generator.add_sentence(sentence42('Sentence 42'))
        self.generator.add_sentence(sentence43('Sentence 43'))
        self.generator.add_sentence(sentence44('Sentence 44'))
        self.generator.add_sentence(sentence45('Sentence 45'))
        self.generator.add_sentence(sentence46('Sentence 46'))
        self.generator.add_sentence(sentence47('Sentence 47'))
        self.generator.add_sentence(sentence48('Sentence 48'))
        self.generator.add_sentence(sentence49('Sentence 49'))
        self.generator.add_sentence(sentence50('Sentence 50'))
        self.generator.add_sentence(sentence51('Sentence 51'))
        self.generator.add_sentence(sentence52('Sentence 52'))
        self.generator.add_sentence(sentence53('Sentence 53'))
        

    def print_sentence_by_name(self, name):
        self.generator.print_sentence_by_name(name)

    def print_all_sentences(self):
        self.generator.print_all_sentences()

    def get_all_sentences(self, min_length, max_length):
        return self.generator.get_all_sentences(min_length, max_length)

    def print_component_data(self, component_key):
        return self.generator.print_component_data(component_key)

    def get_random_word(self, part, length):
        url = "https://wordsapiv1.p.rapidapi.com/words/"
        querystring = {"random":"true"}
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': "d13b08e2c9mshdb21833bede88e1p13c577jsn79fe44d0a6f9"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        js = response.json()
        print(js['word'])