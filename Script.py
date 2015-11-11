#!/usr/bin/env python
from Word import Word
from Parser import Parser
from DF_Writer import DF_Writer

lang = Parser.parse('raws/language_DWARF.txt', 'raws/language_words.txt')
DF_Writer.write(lang[0], lang[1])