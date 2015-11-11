#!/usr/bin/env python
class Word:
    NOUN = 'NOUN'
    VERB = 'VERB'
    ADJ = 'ADJ'

    def __init__(self, word, translation, pof, language):
        self.word = word
        self.word_form = word
        self.translation = translation
        self.pof = pof
        self.language = language

    def format(self, f = '{w}({f}) {t} {p} {l}'):
        return f.format(w=self.word, f=self.word_form, t=self.translation, p=self.pof, l=self.language)

    def __str__(self):
        return self.format()

    def valid(self):
        """
        Checks if word has all required properties
        :return: bool
        """
        if not self.word: return False
        if not self.word_form: return False
        if not self.translation: return False
        if not self.pof: return False
        if not self.language: return False
        return True
