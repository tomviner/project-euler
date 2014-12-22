"""
Starting in the top left corner of a 2x2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20x20 grid?
"""
import math

def moves(x, y, i=1):
    """
    >>> moves(1, 1)
    2
    >>> moves(1, 2)
    3
    >>> moves(2, 2)
    6
    >>> moves(2, 3)
    10
    """
    fac = math.factorial
    return fac(x+y) / (fac(x) * fac(y))

if __name__ == '__main__':
    print moves(20, 20)
