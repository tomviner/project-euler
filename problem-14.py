"""
The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(n):
    """
    >>> list(collatz(13))
    [40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    while n != 1:
        if not n % 2:
            n = n // 2
        else:
            n = 3*n + 1
        yield n

def chain_len(n):
    """
    >>> chain_len(13)
    10
    >>> chain_len(1)
    1
    """
    # count input in chain
    return 1 + sum(1 for x in collatz(n))

# takes 2m22s on netbook, 30s on 4core laptop
# print max(xrange(1, 1000000), key=chain_len)

def inclusive_collatz(n):
    """
    >>> list(inclusive_collatz(13))
    [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    yield n
    for c in collatz(n):
        yield c

def smart_chain_len(n, cache={}):
    """
    >>> smart_chain_len(5)
    6
    >>> smart_chain_len(4)
    3
    >>> smart_chain_len(13)
    10
    >>> smart_chain_len(1)
    1
    """
    seq = []
    # walk tree until a known value found
    for c in inclusive_collatz(n):
        if c in cache:
            break
        else:
            seq.append(c)
    # mark all new values, with count, starting with
    # either 1 or the known value found above
    for i, d in enumerate(reversed(seq), cache.get(c, 0)):
        cache[d] = i + 1
    return cache[n]

# if __name__ == '__main__':
#     # takes just 21s on netbook, 3s on 4 core laptop
    print(max(range(1, 1000000), key=smart_chain_len))
