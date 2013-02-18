directions = itertools.product((-1, 0, 1), repeat=2) # but remove (0, 0)
', '.join('(x+%s, y+%s)' % (dx, dy) for (dx, dy) in directions)
