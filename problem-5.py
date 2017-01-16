"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import itertools

from collections import Counter

from common import prime_factors, product

def divisible_by_range(x, n):
    """
    >>> divisible_by_range(2520, 10)
    True
    >>> divisible_by_range(1000, 10)
    False
    """
    for i in range(n, 1, -1):  # fail quicker by starting high
        if x % i:
            return False
    return True

def smallest_dividible_brute_force(n):
    """
    This takes 11 minutes for n=20 on a netbook!
    >>> smallest_dividible_brute_force(10)
    2520
    """
    for x in itertools.count(n):
        if divisible_by_range(x, n):
            return x

def smallest_dividible(n):
    """
    >>> smallest_dividible(10)
    2520
    """
    factors = Counter()
    for i in range(1, n+1):
        facs = Counter(prime_factors(i))
        for fac, count in list(facs.items()):
            factors[fac] = max(count, factors[fac])
    return product(fac**count for (fac, count) in list(factors.items()))

if __name__ == '__main__':
    print(smallest_dividible(20))
