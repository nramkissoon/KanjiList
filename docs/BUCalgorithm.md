# Break Up Compound Algorithm

In general, kanji words are easy to read and differentiate from
other parts of text because they are separated by kana, punctuation, etc.

However, in Japanese, kanji can be strung together into long
compounds that constitute a single word. 

For example: 国民健康保険料過誤還付通知書

Intuition and experience will tell you that in order to make sense
of such a word, you should break it up into smaller chunks of kanji 
that make smaller words so: 国民、健康、保険料、過誤、還付、通知、書

In order to program this "intuition" to break up compounds in such a way,
two methods are used.

## Method 1
We start with string of characters that make up the compound.

国民健康保険料過誤還付通知書

We check if this string is in the compound dictionary.

If not, we drop the first character and keep checking until
we find a match in the dictionary, or if there are no
matches, then there must be a single kanji left. This match would be:

書

We append this to the back end of a list, drop it from the original
string, and repeat the process. The next dictionary match would be:

通知

After recursively iterating through the string until it is exhausted
we have:

国民、健康、保険料、過誤、還付、通知、書 as elements in the array

## Method 2
Method 2 is the same recursive process as method 1 except we
drop the last character and then check for a match instead of the first.

## Reasoning For Two Methods of Breaking Up A Compound
There are cases (especially where proper names make up a part of the 
compound) where one method returns the correct "intuitive" 
way to break up a compound and the other does not. Depending on the
compound, either or both method may be the correct approach or both
can be "intuitively" wrong ("intuitively" as in how a real person
would break it up). So it is best to have a compound be evaluated 
by both methods and implement a method to judge which method is probably 
the correct one.

## How to Judge "Correctness"
In general, we can assume that a method that breaks up a compound
into less sub-compounds is preferred because less sub-compounds means
the method was able to break up the compound into larger cohesive units.
In the case where both methods break up the compound into an equal amount 
of sub-compounds that are different('abcde' --> 'ab','cde'and 
'abcd','e'), preference should be given to the method with the largest
minimum sub-component ('ab' > 'e'). The reasoning for this is that
a method that breaks up a compound into a lot of individual kanji
is generally not the most ideal because a string broken up into individual kanji
offers little coherence. If neither of the methods are judged to be better
('abcde' --> 'ab','cde' and 'abc','de'), we can choose either one
without worrying about a significant loss in readability or coherence.
