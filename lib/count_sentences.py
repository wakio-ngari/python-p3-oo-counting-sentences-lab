#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self.__value = new_value
        else:
            print("The value must be a string.")
            self.__value = ''

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        temp_value = self.value.replace('!', '.').replace('?', '.')
        sentences = temp_value.split('.')
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)     
  

