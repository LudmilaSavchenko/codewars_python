"""
Vowel Count

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

"""
#var 1
def get_count(sentence):
    sentence = sentence.lower()
    return sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
"""


def getCount(sentence):
    return sum(i in "aeiou" for i in sentence.lower())
