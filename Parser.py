#!/usr/bin/env python
import re
from Word import Word

class Parser:
    @staticmethod
    def parse(language_file, words_file):
        dictionary = Parser.parseWords(words_file)
        return Parser.parseLanguage(language_file, dictionary)

    @staticmethod
    def parseWords(words_file):
        """Parses language_words file
        and extracts word with part of speech
        :rtype: dict
        """
        dictionary = dict()
        lastWord = ''
        with open(words_file) as f:
            for line in f:
                stripped = line.strip()
                if(not stripped.startswith('[')):
                    continue
                if(stripped.startswith('[WORD:')):
                    lastWord = stripped[6:-1]
                elif(':' in stripped):
                    word = Parser.createWord(lastWord, stripped)
                    if word:
                        if word.word in dictionary:
                            dictionary[word.word].append(word)
                        else:
                            dictionary[word.word] = [word,]

        return dictionary

    @staticmethod
    def parseLanguage(language_file, dictionary):
        """
        Parses language file and extracts word translations
        :return:(dict, list)
        """
        first_line = None
        with open(language_file, 'r') as f:
            first_line = f.readline()

        if not first_line.startswith('language_'):
            raise Exception("%s : First line must start from language_SOME_LANGUAGE_NAME" % format(language_file));

        lang = first_line[9:]
        untranslated = list()

        with open(language_file) as f:
            for line in f:
                line = line.strip()
                match = re.search(ur'\[T_WORD:(?P<word>[\w -]+):(?P<translation>\w+)\]$', line)
                if match:
                    wrd = match.group('word')
                    trnslt = match.group('translation')
                    if wrd in dictionary:
                        for dict_word in dictionary[wrd]:
                            dict_word.translation = trnslt
                            dict_word.language = lang
                elif line:
                    # storing all non-empty nontranslated lines
                    untranslated.append(line)

        return (dictionary, untranslated)

    @staticmethod
    def createWord(word_str, pof_line):
        """
        Parses part of speech line
        :rtype: Word
        """
        knownPofs = [Word.NOUN, Word.VERB, Word.ADJ]
        ignored = ['OBJECT', 'ADJ_DIST', 'PREFIX']
        match = re.search(ur'^\[([\w]+):(\w+).*\]$', pof_line)
        if not match:
            raise Exception('Unknown line format: %s' % format(pof_line))
        pof = match.group(1)
        if pof not in knownPofs and pof not in ignored:
            print pof_line
            raise Exception('Unknown pof: %s' % format(pof))
        if pof in ignored:
            return None
        word = Word(word_str, '', pof, '')
        word.word_form = match.group(2).capitalize()
        return word
