# JLPT Algorithm 

In order to filter words by their JLPT level, we need to find the JLPT 
levels of all individual kanji that make up a word and create a function 
that incorporates these several values as inputs and outputs a single integer value
ranging from 0 to 5. 

Getting the JLPT is simple for individual kanji.
For cases when there is no JLPT data available, assume a JLPT of 0
(even though 0 is not an official value)

To estimate a JLPT value for kanji compounds, the most accurate way 
to estimate is to take the average of the JLPT values and return that value.

However, just returning the average creates problems for cases where the 
average is just below the cutoff JLPT needed to be included in an output.

For Example:

Consider a kanji compound x with JLPT levels 1,1,1,2.

The average JLPT for x is 1.25

The way filtering is implemented is such that the JLPT level
indicated by the user is the maximum value a JLPT is allowed to be in order to be
in the ouput.

So a JLPT cutoff of 2 would include x, but a cutoff of 1 will not.

A user who indicates a JLPT level of 1 wants kanji words of JLPT 1
to be included in the output. x contains 3 kanji with JLPT 1 but will not 
be included. 

Because of this, we round the averages to the nearest whole number,
solving this problem.

Round does not make the JLPT filtering foolproof however.
A kanji compound y with JLPT levels of 1,1,1,1,2,2,2,3 will
evaluate to a overall JLPT of 2 even though a user may not be able to 
read the kanji with JLPT 1. Despite this, a reader with JLPT 2 level ability
should be able to piece together the overall meaning of y. 

This can be seenas a benefit as the JLPT filtering does not 
allow words the user can piece together vie context to be in the output. The result 
of such filtering means the reader cannot be completely dependant on
the output list, pressuring them think about what the meanings of some words
are and passively increasing their comprehension abilities
without distracting from the experience of reading the text. 

In real life, even Japanese do not know every kanji they may encounter, 
but they are able to derive meanings from context anyways so this skill
is crucial for learning Japanese.