"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
import itertools

def pyth_trips(max_val):
    """
    >>> list(pyth_trips(5))
    [(3, 4, 5)]
    """
    sides = itertools.combinations_with_replacement(range(1, max_val+1), 2)
    for a, b in sides:
        c = math.sqrt(a**2 + b**2)
        int_c = int(c)
        if int_c == c:
            yield a, b, int_c

if __name__ == '__main__':
    for a, b, c in pyth_trips(1000):
        if a + b + c == 1000:
            print a * b * c
