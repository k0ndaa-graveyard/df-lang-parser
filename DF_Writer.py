#!/usr/bin/env python
import os.path

class DF_Writer:
    @staticmethod
    def write(dictionary, unparsed, outputdir = 'output', output_format = 'my-js-readable'):
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        translation_file =  os.path.join(outputdir, 'language.txt')
        if output_format == 'my-js-readable':
            DF_Writer.write_my_format(dictionary, translation_file)
        else:
            print 'Unknown format %s' % format(output_format)
            return

        no_translate_file = os.path.join(outputdir, 'Non-translated.txt')
        DF_Writer.writeUnparsed(unparsed, no_translate_file)

        invalid_words_file = os.path.join(outputdir, 'broken-words.txt')
        DF_Writer.writeInvalidWords(dictionary, invalid_words_file)


    @staticmethod
    def writeUnparsed(unparsed, outpufile):
        with open(outpufile, 'w') as file:
            for line in unparsed:
                file.writelines(line)

    @staticmethod
    def writeInvalidWords(dictionary, outputfile):
        with open(outputfile, 'w') as f:
            for words in dictionary:
                for word in dictionary[words]:
                    if not word.valid():
                        f.write(word.format())
                        f.write(os.linesep)

    @staticmethod
    def write_my_format(dictionary, outpufile):
        frmt = "new DFNames.Word('{f}', '{t}', '{p}'),"
        with open(outpufile, 'w') as f:
            for words in dictionary:
                for word in dictionary[words]:
                    if word.valid():
                        f.write(word.format(frmt))
                        f.write(os.linesep)