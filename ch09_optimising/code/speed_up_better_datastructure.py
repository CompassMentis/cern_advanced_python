import timeit

names_as_list = []
for name in 'Fred', 'Jo', 'Sam', 'Alex':
    for i in range(10_000):
        names_as_list.append(f'{name}{i:06}')

names_as_set = set(names_as_list)
assert len(names_as_list) == len(names_as_set) == 40_000


def before():
    for _ in range(100):
        if 'Si' in names_as_list:
            a = 1


def after():
    for _ in range(100):
        if 'Si' in names_as_set:
            a = 1


print(timeit.timeit('before()', globals=globals(), number=100))
# 3.059100901999045

print(timeit.timeit('after()', globals=globals(), number=100))
# 0.00019055899974773638
