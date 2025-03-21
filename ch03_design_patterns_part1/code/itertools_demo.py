import itertools


def show(iterator, limit=10):
    print(list(itertools.islice(iterator, limit)))


show(range(100))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

show(itertools.count(5))
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

show(itertools.chain(range(4), range(10, 15)))
# [0, 1, 2, 3, 10, 11, 12, 13, 14]

show(itertools.repeat(10, 7))
# [10, 10, 10, 10, 10, 10, 10]

show(itertools.accumulate([1, 2, 3, 4]))
# [1, 3, 6, 10]

show(itertools.cycle('ABC'))
# ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']

show(itertools.pairwise(range(20)))
# [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
# (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
