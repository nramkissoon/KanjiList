""" Methods for parsing a text for kanji words and building a dictionary of words to be searched and their
corresponding line appearances in the original text
"""


def kanji_check(character):
    """ Determines if the character parameter is a kanji character based on UTF-8 code"""

    if (ord(character) >= ord('\u4e00')) and (ord(character) <= ord('\u9faf')):
        return True
    else:
        return False


def get_kanji_words(text):
    """ Function creates a list of all individual and compound kanji that appear in the text parameter"""

    ret_list = []
    a = ""
    for i in text:
        if kanji_check(i):
            a += i
        else:
            if not (a == ""):
                ret_list.append(a)
                a = ""
    if not (a == ""):  # checks if last character is a kanji
        ret_list.append(a)
    return ret_list


def get_kanji_byorder(text):
    """ Gets all kanji words in the order that they appear in the original text"""

    ret_list = []
    words = get_kanji_words(text)
    for i in words:
        for j in i:
            if j not in ret_list:
                ret_list.append(j)
    return ret_list


def remove_duplicates(kanji_list):
    """ Removes duplicate kanji words"""

    ret_list = []
    for i in kanji_list:
        for j in i:
            if j not in ret_list:
                ret_list.append(j)
    return ret_list


def get_kanji_byline(lines):
    """ Returns a nested list that groups kanji words by the line they are in"""
    ret_list = []
    for i in lines:
        ret_list.append(get_kanji_words(i))
    return ret_list


def create_kanji_line_dict(textlines):
    """ Creates a dictionary of all kanji to be searched and their corresponding line appearances"""

    kanji_line_dict = {}
    keys = remove_duplicates(get_kanji_byline(textlines))
    for i in keys:
        kanji_line_dict[i] = []
    lines = get_kanji_byline(textlines)
    for i in lines:
        for keys in kanji_line_dict:
            for j in i:
                if keys == j:
                    kanji_line_dict[keys].append(lines.index(i) + 1)
    return kanji_line_dict
