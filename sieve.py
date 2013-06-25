import itertools

def sieve(ns):
    """
    Sieve of eratosthenes
    (Work in progress, currently just returns odd numbers)
    """
    n = list(itertools.islice(ns, 1))[0]
    yield n
    for item in itertools.ifilter(lambda x: x % n != 0, ns):
        yield item

ps = sieve(itertools.count(2))
print list(itertools.islice(ps, 100))
