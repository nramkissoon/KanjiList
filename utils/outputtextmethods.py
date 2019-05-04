"""Methods for formatting text to be returned as the output for the program."""


def single_kanji_output_text(output_dict, i, is_component=False, meanings=True, yomi=True, nanori=False,
                             frequency=False, jlpt=False):
    """Specifically deals with individual kanji cases"""

    if is_component:
        ret_str = "    " + i + '\n'  # extra indenting for better readability
    else:
        ret_str = i + ": Lines: " + str(output_dict[i]["lines"])[1:-1] + "\n"
    try:
        if meanings:
            ret_str += "    Meanings: " + str(output_dict[i]["meaning"])[1:-1] + "\n"
        if yomi:
            ret_str += "    Onyomi: {0}\n    Kunyomi: {1}\n".format(str(output_dict[i]["onyomi"])[1:-1],
                                                                    str(output_dict[i]["kunyomi"])[1:-1])
        if nanori:
            ret_str += "    Nanori: " + str(output_dict[i]["nanori"])[1:-1] + "\n"
        if frequency:
            ret_str += "    Frequency: " + str(output_dict[i]["freq"])[1:-1] + "\n"
        if jlpt:
            ret_str += "    JLPT: " + str(output_dict[i]["jlpt"])[1:-1] + "\n"
        ret_str += "\n"
        return ret_str
    except KeyError:
        return "    " + i + "    N/A  \n"


def compound_kanji_output_text(output_dict, i, is_component=False, meanings=True, yomi=True, jlpt=False):
    """Specifically deals with compound kanji cases."""

    if is_component:
        ret_str = "    " + i + '\n'
    else:
        ret_str = i + ": Lines: " + str(output_dict[i]["lines"])[1:-1] + "\n"
    try:
        if meanings:
            ret_str += "    Meanings: " + str(output_dict[i]["meaning"])[1:-1] + "\n"
        if yomi:
            ret_str += "    Reading: " + str(output_dict[i]["reading"]) + "\n"
        if jlpt:
            ret_str += "    JLPT: " + str(output_dict[i]["jlpt"])[1:-1] + "\n"
    except KeyError:
        if meanings or yomi:
            ret_str += "    Proper Noun: " + str(output_dict[i]["reading"])[1:-1] + "\n"
        if jlpt:
            ret_str += "    JLPT: " + str(output_dict[i]["jlpt"])[1:-1] + "\n"
    return ret_str + "\n"


def create_output_text(output_dict, i, w_meanings=True, w_yomi=True, w_nanori=False, w_frequency=False, w_jlpt=False):
    """Creates an output text entry for a kanji word
        Keyword arguments for this function will be user-generated and passed on to sub-functions"""

    if len(i) == 1:
        ret_str = single_kanji_output_text\
            (output_dict, i, meanings=w_meanings, yomi=w_yomi, nanori=w_nanori, frequency=w_frequency, jlpt=w_jlpt)
    else:
        if "kanji components" in output_dict[i]:
            start = (i + ": Lines: " + str(output_dict[i]["lines"])[1:-1] + "\n")
            str_list = [start]
            for component in output_dict[i]['kanji components']:
                if len(component) == 1:
                    component_str = single_kanji_output_text(output_dict[i]["kanji components"], component,
                                                             is_component=True, meanings=w_meanings, yomi=w_yomi,
                                                             nanori=w_nanori, frequency=w_frequency, jlpt=w_jlpt)
                else:
                    component_str = compound_kanji_output_text(output_dict[i]["kanji components"], component,
                                                               is_component=True, meanings=w_meanings,
                                                               yomi=w_yomi, jlpt=w_jlpt)
                str_list.append(component_str)
            ret_str = ''.join(str_list)
        else:
            ret_str = compound_kanji_output_text(output_dict, i, meanings=w_meanings, yomi=w_yomi, jlpt=w_jlpt)
    return ret_str + 100 * '-' + '\n'  # visual separator for better readability
