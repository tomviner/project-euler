import itertools

def s(ns):
    n = list(itertools.islice(ns, 1))[0]
    yield n
    for item in itertools.ifilter(lambda x: x % n != 0, ns):
        yield item

ps = s(itertools.count(2))
print list(itertools.islice(ps, 100))
