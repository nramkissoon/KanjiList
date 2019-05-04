"""Methods for getting data for each kanji word that appears in the input text"""

from .dictmethods import *
from statistics import mean


def break_up_compound(compound_dict, compound):
    """Breaks up a compound kanji word into sub-parts that habe entries in the compound_dict
        See BUCalgorithm in docs"""

    a = buc_method1(compound_dict, compound)
    b = buc_method2(compound_dict, compound)
    if len(a) < len(b):  # Breaking up a kanji compound into less chunks is preferred
        return a
    elif len(b) < len(a):
        return b
    else:  # If amount of chunks are equal, return the one with chunks of longer length
        if len(min(a, key=len)) > len(min(b, key=len)):
            return a
        elif len(min(a, key=len)) < len(min(b, key=len)):
            return b
    return b


def buc_method1(compound_dict, compound, ret_list=None):
    """Helper for break_up_compound"""

    if ret_list is None:
        ret_list = []
    if compound == "":
        return
    a = compound
    i = 0
    while a not in compound_dict and len(a) != 1:
        i += 1
        a = a[1:]
    ret_list = [a] + ret_list
    compound = compound[:-len(a)]
    if len(compound) == 0:
        ret_list.append(compound)
        return ret_list[:-1]
    return buc_method1(compound_dict, compound, ret_list)


def buc_method2(compound_dict, compound, ret_list=None):
    """Helper for break_up_compound"""

    if ret_list is None:
        ret_list = []
    if compound == "":
        return
    a = compound
    i = 0
    while a not in compound_dict and len(a) != 1:
        i += 1
        a = a[0:-1]
    ret_list.append(a)
    compound = compound[len(compound) - i:]
    if len(compound) == 0:
        ret_list.append(compound)
        return ret_list[:-1]
    return buc_method2(compound_dict, compound, ret_list)


def build_compound_dict_keys(kanji_list, compound_dict):
    """Creates a dictionary with keys of all kanji words from input text"""

    ret_dict = {}
    for i in kanji_list:
        if len(i) == 1:
            ret_dict[i] = {}
            ret_dict[i]['lines'] = []
        else:
            ret_dict[i] = {}
            ret_dict[i]['lines'] = []
            if not in_dict(i, compound_dict):
                keys = break_up_compound(compound_dict, i)
                for j in keys:
                    if j != i:
                        try:
                            ret_dict[i]["kanji components"][j] = []
                        except KeyError:
                            ret_dict[i]["kanji components"] = {}
                            ret_dict[i]["kanji components"][j] = []
    return ret_dict


def get_kanji_data(kanji_list, kanji_dict, compound_dict, kanji_line_dict):
    """Takes a list of kanji and creates a dictionary with relevant data for each entry"""

    ret_dict = {}
    for i in kanji_list:
        if len(i) > 1:
            if "kanji components" not in kanji_list[i]:
                ret_dict[i] = {}
                ret_dict[i] = compound_dict[i]
            else:
                ret_dict[i] = {}
                ret_dict[i]["kanji components"] = {}
                for j in kanji_list[i]["kanji components"]:
                    if len(j) == 1:
                        try:
                            ret_dict[i]["kanji components"][j] = kanji_dict[j]
                        except KeyError:
                            ret_dict[i]["kanji components"][j] = "N/A"
                    else:
                        ret_dict[i]["kanji components"][j] = {}
                        ret_dict[i]["kanji components"][j] = compound_dict[j]
        else:
            try:
                ret_dict[i] = kanji_dict[i]
            except KeyError:
                ret_dict[i] = " N/A "
    for i in ret_dict:
        lines = []
        for line in kanji_line_dict[i]:
            if line not in lines:
                lines.append(line)
        if len(lines) > 10:
            ret_dict[i]['lines'] = lines[:9] + ['...']  # for better readability
        else:
            ret_dict[i]['lines'] = lines
    return ret_dict


def get_jlpt(output_dict, entry):
    """Determines the jlpt level of a kanji word
        See JLPTalgorithm in docs"""

    if len(entry) == 1:
        if output_dict[entry] == "N/A":
            return 0
        elif output_dict[entry]['jlpt'] == ["N/A"]:
            return 0
        else:
            try:
                return int(output_dict[entry]['jlpt'][0])
            except ValueError:
                return 0
    elif "kanji components" not in output_dict[entry]:
        jlpt_list = []
        for jlpt in output_dict[entry]['jlpt']:
            try:
                jlpt_list.append(int(jlpt))
            except ValueError:
                jlpt_list.append(0)
        return round(mean(jlpt_list))
    else:
        jlpt_list = []
        for component in output_dict[entry]["kanji components"]:
            if output_dict[entry]["kanji components"][component] == "N/A":
                jlpt_list.append(0)
            else:
                for jlpt in output_dict[entry]["kanji components"][component]['jlpt']:
                    try:
                        jlpt_list.append(int(jlpt))
                    except ValueError:
                        jlpt_list.append(0)
        return round(mean(jlpt_list))
