import requests
import json
import random
import time
import string
import names

# A central place where I can add everything once
# Let's me play with sentence structures independently
# Ties everything together
# 1 - instantiates a geenrator object
# 2 - makes sentences and push them into the generator

# Sentence construction
from sentence_generator import sentence_generator
from sentences.sentence1 import sentence1
from sentences.sentence2 import sentence2

class scifisanity(object):
    generator = None

    def __init__(self):
        self.generator = sentence_generator()
        self.generator.populate_components()

        self.generator.add_sentence(sentence1('Sentence 1'))
        self.generator.add_sentence(sentence2("Sentence 2"))

    def print_sentence_by_name(self, name):
        self.generator.print_sentence_by_name(name)

    def print_all_sentences(self):
        self.generator.print_all_sentences()

    def get_all_sentences(self, max_length):
        return self.generator.get_all_sentences(max_length)