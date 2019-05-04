"""Main script for KanjiList Project"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from utils.Output import Output_txtfile, Output_clip
from utils.dictmethods import *
import pyperclip


def main():
    q = False
    kanji_dict = get_kanji_dict()
    compound_dict = get_compound_dict()
    print("KanjiList Program")
    while not q:
        print("\nCommands:\n"
              + "q: Quit the Program\n"
              + "f: Get input text from a text file.\n"
              + "c: Get input text from clipboard.\n\n")
        key = input("Please Enter a Command (q/f/c): ")
        while key not in ['q', 'f', 'c']:
            key = input("Invalid Command Entered (Please try again): ")
        if key == 'q':
            print('\nGoodbye.')
            break
        jlpt = input("Enter a JLPT level (0/1/2/3/4/5): ")
        while jlpt not in ['0', '1', '2', '3', '4', '5']:
            print("\nInvalid Input")
            jlpt = input("Enter a JLPT level (0/1/2/3/4/5): ")
        jlpt = int(jlpt)
        fields = {'w_meanings': True, 'w_yomi': True, 'w_nanori': False, 'w_frequency': False, 'w_jlpt': False}
        change_fields = input("Default output text include meanings and readings, but not nanori, frequency,\n" +
                              " and jlpt. Change default output? (y/n): ")
        while change_fields not in ['y', 'n']:
            print('\nInvalid Input')
            change_fields = input("Change default output? (y/n): ")
        if change_fields == "y":
            for field in fields:
                selection = input("Include " + field[2:] + " in KanjiList? (y/n): ")
                while selection not in ['y', 'n']:
                    print('\nInvalid Input')
                    selection = input("Include " + field[2:] + " in KanjiList? (y/n): ")
                if selection == 'y':
                    fields[field] = True
                else:
                    fields[field] = False
        if key == 'f':
            root = Tk()
            root.withdraw()
            try:
                filename = askopenfilename(title='Choose a file')
                root.update()
                output = Output_txtfile(filename, kanji_dict, compound_dict, jlpt)
                output.change_kwargs(fields)
                output.write_outputfile()
                print("Created new KanjiList text file for: " + output.filename)
            except FileNotFoundError:
                print('Action Canceled\n')
            key = input("Press any key to continue creating KanjiLists or press 'q' to quit: ")
            if key == 'q':
                print('\nGoodbye.')
                break
        elif key == 'c':
            cont = input("Have you copied some text to get a KanjiList for? (y/n): ")
            while cont not in ['y', 'n']:
                print('\nInvalid Input')
                cont = input("Have you copied some text to get a KanjiList for? (y/n): ")
            if cont == 'y':
                text = pyperclip.paste()
                output = Output_clip(text, kanji_dict, compound_dict, jlpt)
                output.change_kwargs(fields)
                output.create_output_lines()
                pyperclip.copy(output.output_lines)
                print('\nCopied KanjiList to clipboard.')
                print(output.output_lines)
            key = input("\nPress any key to continue creating KanjiLists or press 'q' to quit: ")
            if key == 'q':
                print('\nGoodbye.')
                break


if __name__ == '__main__':
    main()
