"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import itertools

from common import primes

def nth_prime(n):
    """
    >>> list(primes(n=6))
    [2, 3, 5, 7, 11, 13]
    >>> nth_prime(6)
    13
    """
    return list(itertools.islice(primes(n=n), n-1, n))[0]

if __name__ == '__main__':
    print(nth_prime(10001))
