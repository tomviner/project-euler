"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from common import primes

def sum_of_primes(n):
    """
    >>> sum_of_primes(10)
    17
    """
    return sum(primes(max_val=n))


if __name__ == '__main__':
    print(sum_of_primes(2000000))
