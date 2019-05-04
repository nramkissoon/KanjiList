# KanjiList
## Project Summary
KanjiList is a command line program meant to read Japanese text as an input and 
output a list of kanji words that appear in the input text along with 
their respective meanings, readings, etc. The data for words comes from 
the [JMdict project](http://www.edrdg.org/jmdict/edict_doc.html) and 
the [KANJIDIC Project](http://www.edrdg.org/wiki/index.php/KANJIDIC_Project).

The intended users of this program are Japanese language learners that are barred 
from reading Japanese text such as news articles because of a lack in kanji skills.

## How To Use
By running *kanjilist.py*, the user will be prompted to provide 
preferences for what the output text should include and indicate from
where the program will get text input. Currently, the user can 
read in a text file and output a text file in the same directory containing 
the output text [(see samples)](samples), or the user can copy text onto their clipboard, run the 
program, and the output text will then be copied onto the clipboard and 
outputted to the terminal.

## Output Preferences
### JLPT
The user will be prompted to indicate what JLPT level will be used to 
filter out kanji words. Kanji are ranked from levels 1 through 5 depending 
on their frequency and how early one is expected to know it. The higher the 
rank, the 'easier' the kanji is. If the user selects level 5, all kanji
will be included in the output. If the user selects 3, all individual kanji
ranked 1 to 3 will be included as well as any compounds where the rounded mean
of its individual components' JLPT is ranked 1 to 3. An extra option 0
is included to create output texts for kanji that are so uncommon that they 
are not ranked by the JLPT system. 

[For a detailed explanation for how JLPT filtering works.](docs/JLPTalgorithm.md)

### Other Kanji Information

The user has the ability to change what information will be including 
in the final output. The user can choose to include/not include: meainings,
readings, nanori, frequency, and JLPT. The default is set so that only 
meanings and readings will be outputted. 


## License Information
This program would not be possible without the JMdict and KANJIDIC projects as 
all data in the json dictionaries of this project is extracted and adapted from them.
Licensing information regarding the JMdict and KANJIDIC projects can 
be found [here](http://www.edrdg.org/edrdg/licence.html).







