"""
Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""
import json
import string

def score_word(word):
    """
    >>> score_word('COLIN')
    53
    """
    return sum(string.ascii_uppercase.index(letter)+1 for letter in word.upper())

def score_string(s):
    """
    >>> score_string('"COLIN"')
    53
    >>> score_string('"A","COLIN"')
    107
    """
    words = sorted(json.loads('[{}]'.format(s)))
    return sum(
        row * score_word(word)
        for row, word in enumerate(words, 1)
    )

if __name__ == '__main__':
    print(score_string(open('p022_names.txt').read()))
