import itertools

def sieve(ns):
    """
    Sieve of eratosthenes
    (Work in progress, currently just returns odd numbers)
    """
    n = list(itertools.islice(ns, 1))[0]
    yield n
    for item in [x for x in ns if x % n != 0]:
        yield item

if __name__ == '__main__':
    ps = sieve(itertools.count(2))
    print(list(itertools.islice(ps, 100)))
