# parent class
# common functionality that every sentence will need

class base_sentence(object):
    sentence_name = ""

    def __init__(self, sentence_name):
        self.sentence_name = sentence_name

    def get_name(self):
        return self.sentence_name