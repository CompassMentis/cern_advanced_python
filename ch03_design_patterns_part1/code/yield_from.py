def large_numbers():
    yield 100
    yield 200
    yield 300


def all_numbers():
    yield from 'Hello'
    yield from range(1, 4)
    yield from large_numbers()
    yield from (10 ** x for x in range(3))


def small_numbers_plus():
    yield from large_numbers()
    yield 4
    yield 5


print(list(all_numbers()))
# ['H', 'e', 'l', 'l', 'o',
# 1, 2, 3, 100, 200, 300, 1, 10, 100]

print(list(small_numbers_plus()))
# [100, 200, 300, 4, 5]
