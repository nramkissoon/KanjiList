"""Methods for dealing with the compound_dict and kanji_dict"""

import json
import os

file_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(file_path, os.path.pardir))
data_path = os.path.join(project_path, 'data')


def get_kanji_dict():
    """ Retrieves the kanji dictionary json file if it exists"""

    try:
        ff = open(data_path + "/kanji_dict.json", "rb")
        kanji_dict = json.load(ff)
        ff.close()
        return kanji_dict
    except FileNotFoundError:
        print("kanji_dict.json not found in 'data' directory")
        print("Make sure kanji_dict.json has been created")
        raise FileNotFoundError


def get_compound_dict():
    """ Retrieves the kanji compound dictionary json file if it exists"""

    try:
        ff = open(data_path + "/compound_dict.json", "rb")
        kanji_dict = json.load(ff)
        ff.close()
        return kanji_dict
    except FileNotFoundError:
        print("compound_dict.json not found in 'data' directory")
        print("Make sure compound_dict.json has been created")
        raise FileNotFoundError


def in_dict(compound, compound_dict):
    if str(compound) in compound_dict:
        return True
    return False
