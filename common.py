import math
import itertools
import operator
from functools import reduce


def product(ns):
    """
    >>> product((26, 63, 78, 14))
    1788696
    """
    return reduce(operator.mul, ns)

def is_prime(n=100, cache={}):
    """
    >>> [is_prime(n) for n in (2, 3, 5, 7, 11, 13, 17, 19)]
    [True, True, True, True, True, True, True, True]
    >>> [is_prime(n) for n in (0, 1, 4, 6, 8, 9, 21)]
    [False, False, False, False, False, False, False]
    """
    if n in cache:
        return cache[n]
    if n <= 2:
        cache[n] = n == 2
        return n == 2
    top = int(math.ceil(math.sqrt(n)))
    # 2, 3, 5, 7, 9, 11, ... top
    for i in [2] + list(range(3, top + 1, 2)):
        if not n % i:
            cache[n] = False
            return False
    cache[n] = True
    return True

def primes(max_val=None, n=None):
    """
    >>> list(primes(n=10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> list(primes(max_val=23))
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """
    prime_gen = filter(is_prime, itertools.count(1))
    prime_gen = itertools.takewhile(
        lambda x: max_val is None or x <= max_val, prime_gen)
    return itertools.islice(prime_gen, n)

def prime_factors(n):
    """
    >>> prime_factors(13195)
    [5, 7, 13, 29]
    >>> prime_factors(81)
    [3, 3, 3, 3]
    >>> prime_factors(60)
    [2, 2, 3, 5]
    >>> prime_factors(5)
    [5]
    """
    left = n
    facs = []
    while 1 < left:
        top = int(math.ceil(math.sqrt(left)))
        for i in primes(top + 1):
            if not left % i:
                left = math.floor(left / i)
                facs.append(i)
                if left == 1:
                    break
        else:
            if is_prime(left):
                facs.append(left)
                break
    return sorted(facs)
