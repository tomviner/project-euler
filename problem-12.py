"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
from itertools import count

import pytest


def gen_triangle():
    """
    >>> list(islice(gen_triangle(), 10))
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    """
    tot = 0
    for n in count(1):
        tot += n
        yield tot

def gen_divisors(n):
    """
    >>> list(gen_divisors(28))
    [1, 2, 4, 7, 14, 28]
    """
    import math

    yield 1
    if n == 1:
        return
    sqrt = int(math.sqrt(n))
    divs = []
    if sqrt > 1 and not n % sqrt:
        # we don't want to count perfect squares twice
        divs.append(sqrt)

    for i in range(2, sqrt):
        rem = n % i
        if not rem:
            yield i
            divs.append(n // i)
    for i in reversed(divs):
        yield i
    yield n

def get_divisor_count(n):
    """
    >>> get_divisor_count(28)
    6
    """
    import math

    if n == 1:
        return 1
    tot = 2
    sqrt = int(math.sqrt(n))
    if sqrt > 1 and not n % sqrt:
        # we don't want to count perfect squares twice
        tot += 1
    tot += sum(2 for i in range(2, sqrt) if not n % i)
    return tot

def get_divisor_count_pf(n):
    # try prime factor approach from project euler guide to this question
    from common import prime_factors, product
    from collections import Counter
    if n == 1:
        return 1
    pfs = prime_factors(n)
    pfc = Counter(pfs)
    num_divs = product(pow+1 for (base, pow) in list(pfc.items()))
    return num_divs

def first_triangle_by_factors(n):
    """
    >>> first_triangle_by_factors(5)
    28
    """
    triangle = 0
    for i in count(1):
        triangle += i
        if get_divisor_count(triangle) > n:
            return triangle


DIVISOR_TESTS = (
    (1, [1]),
    (3, [1, 3]),
    (25, [1, 5, 25]),
    (28, [1, 2, 4, 7, 14, 28]),
    (102, [1, 2, 3, 6, 17, 34, 51, 102]),
    (1003, [1, 17, 59, 1003]),
    (1005, [1, 3, 5, 15, 67, 201, 335, 1005]),
)

@pytest.mark.parametrize('n, expected', DIVISOR_TESTS)
def test_gen_divisors(n, expected):
    assert list(gen_divisors(n)) == expected

@pytest.mark.parametrize('n, expected', DIVISOR_TESTS)
def test_get_divisor_count(n, expected):
    assert get_divisor_count(n) == len(expected)

@pytest.mark.parametrize('n, expected', DIVISOR_TESTS)
def test_get_divisor_count_pf(n, expected):
    assert get_divisor_count_pf(n) == len(expected)


if __name__ == '__main__':
    print(first_triangle_by_factors(500))
