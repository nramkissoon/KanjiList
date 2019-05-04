"""Classes for the two types of output for the function"""

from .searchmethods import *
from .inputparsermethods import *
from .outputtextmethods import *


class Output_txtfile:
    """Class for output in cases where the input text originates from a text file."""

    filename = ""
    outputfilename = ""
    kanji_line_dict = {}
    output_dict = {}
    jlpt_level = 0
    output_text_kwargs = {'w_meanings': True, 'w_yomi': True, 'w_nanori': False, 'w_frequency': False, 'w_jlpt': False}

    def change_kwargs(self, kwarg_dict):
        """Function that will change what data will be returned based on user choice"""

        self.output_text_kwargs = kwarg_dict

    def __init__(self, filename, kanji_dict, compound_dict, jlpt):
        self.filename = filename
        f = open(filename, 'r')
        self.kanji_line_dict = create_kanji_line_dict(f.readlines())
        f.close()
        self.output_dict = get_kanji_data(
            build_compound_dict_keys(self.kanji_line_dict,
                                     compound_dict),
            kanji_dict, compound_dict, self.kanji_line_dict)
        self.jlpt_level = jlpt
        self.outputfilename = filename[:-4] + "-KanjiList" + "JLPT" + str(self.jlpt_level) + ".txt"

    def create_output_lines_gen(self):
        for i in self.kanji_line_dict:
            if self.jlpt_level == 5:
                yield create_output_text(self.output_dict, i, **self.output_text_kwargs)
            else:
                if get_jlpt(self.output_dict, i) <= self.jlpt_level:
                    yield create_output_text(self.output_dict, i, **self.output_text_kwargs)

    def write_outputfile(self):
        outputfile = open(self.outputfilename, 'w')
        outputfile.write(self.filename + '\n\n' + "JLPT Level: " + str(self.jlpt_level) + '\n\n')
        for i in self.create_output_lines_gen():
            outputfile.write(i)
        outputfile.close()


class Output_clip:
    """Class for output in cases where the input text originates from the clipboard"""

    kanji_line_dict = {}
    output_dict = {}
    jlpt_level = 0
    output_text_kwargs = {'w_meanings': True, 'w_yomi': True, 'w_nanori': False, 'w_frequency': False, 'w_jlpt': False}
    output_lines = ''

    def change_kwargs(self, kwarg_dict):
        """Function that will change what data will be returned based on user choice"""

        self.output_text_kwargs = kwarg_dict

    def __init__(self, clipboard_text, kanji_dict, compound_dict, jlpt):
        self.kanji_line_dict = create_kanji_line_dict(clipboard_text.splitlines())
        self.output_dict = get_kanji_data(
            build_compound_dict_keys(
                self.kanji_line_dict,
                compound_dict),
            kanji_dict, compound_dict, self.kanji_line_dict)
        self.jlpt_level = jlpt

    def create_output_lines_gen(self):
        for i in self.kanji_line_dict:
            if self.jlpt_level == 5:
                yield create_output_text(self.output_dict, i, **self.output_text_kwargs)
            else:
                if get_jlpt(self.output_dict, i) <= self.jlpt_level:
                    yield create_output_text(self.output_dict, i, **self.output_text_kwargs)

    def create_output_lines(self):
        for i in self.create_output_lines_gen():
            self.output_lines += i
