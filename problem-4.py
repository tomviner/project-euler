"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math

def is_palindrome(n):
    """
    >>> is_palindrome(9009)
    True
    >>> is_palindrome(12321)
    True
    >>> is_palindrome(1212)
    False
    """
    s = str(n)
    m = int(math.floor(len(s) / 2.0))
    # compare 1st half to reverse of 2nd half
    return s[:m] == s[:-m-1:-1]

def product_pairs(max_n):
    """
    Unfortunately this doesn't always yield pairs whose product is decreasing
    >>> list(product_pairs(2))
    [4, 2, 1]
    """
    for x in range(max_n, 0, -1):
        for y in range(max_n, x-1, -1):
            yield y * x

def palindrome_products(digits):
    """
    >>> max(palindrome_products(2))
    9009
    """
    for product in product_pairs(int('9'*digits)):
        if is_palindrome(product):
            yield product

if __name__ == '__main__':
    print max(palindrome_products(3))
