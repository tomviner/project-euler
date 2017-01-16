"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n):
    """
    >>> sum_of_squares(10)
    385
    """
    return sum(i**2 for i in range(1, n+1))

def square_of_sum(n):
    """
    >>> square_of_sum(10)
    3025
    """
    return sum(range(1, n+1))**2

def diff(n):
    """
    >>> diff(10)
    2640
    """
    return square_of_sum(n) - sum_of_squares(n)

if __name__ == '__main__':
    print(diff(100))
