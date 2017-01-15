"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""
import pytest

WORDS = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'hundred',
    '1000': 'thousand',
    'and': 'and',
}
def number_letter_count(n):
    parts = (
        # thousands, hundreds, tens, units
        # m, h, t, u
        # units
        lambda n, m, h, t, u: WORDS[u] if t != '1' else '',
        # decades
        lambda n, m, h, t, u: (
            WORDS.get(f'{t}{u}', WORDS.get(t + '0', ''))
        ),
        # and
        lambda n, m, h, t, u: WORDS['and'] if (
            n >= 100 and (int(t) or int(u)))
        else '',
        # hundred
        lambda n, m, h, t, u: WORDS['100'] if int(h) else '',
        # hundreds
        lambda n, m, h, t, u: WORDS[h],
        # thousand
        lambda n, m, h, t, u: WORDS['1000'] if int(m) else '',
        # thousands
        lambda n, m, h, t, u: WORDS[m],
    )
    nstr = '{:04d}'.format(n)
    words = []
    for part in parts:
        words.append(part(n, *nstr))
    text = ' '.join(words[::-1])
    print(n, text)
    return len(text.replace(' ', ''))

@pytest.mark.parametrize('n, letters', [
    # one
    (1, 3),
    # eleven
    (11, 6),
    # twelve
    (12, 6),
    # thirteen
    (13, 8),
    # fourteen
    (14, 8),
    # fifteen
    (15, 7),
    # sixteen
    (16, 7),
    # seventeen
    (17, 9),
    # eighteen
    (18, 8),
    # nineteen
    (19, 8),
    # twenty
    (20, 6),
    # twenty-one
    (21, 9),
    # three hundred and forty-two
    (342, 23),
    # one hundred and fifteen
    (115, 20),
    # one thousand
    (1000, 11),
    # nine thousand nine hundred and ninety nine
    (9999, 36),
])
def test_number_letter_count(n, letters):
    assert number_letter_count(n) == letters


if __name__ == '__main__':
    print(sum(number_letter_count(n) for n in range(1, 1001)))
