import requests
import json
import random
import time
import string
import names

# Sentence construction
from scifisanity import scifisanity

bot = scifisanity()

# Print all the sentences the generator in scifisanity knows about
#bot.print_all_sentences()

# Print just one sentence from one of the sentences registered with the generator inside scifisanity
bot.print_sentence_by_name('Sentence 57')

#bot.print_component_data('drifting_consequence')

#bot.get_random_word('verb', 10)