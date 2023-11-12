import timeit


def before():
    def add_to_roots(roots, i):
        roots.append(i ** 0.5)
    roots = []
    for i in range(100):
        add_to_roots(roots, i)
    return roots


def after():
    roots = []
    for i in range(100):
        roots.append(i ** 0.5)
    return roots


print(timeit.timeit('before()', globals=globals(), number=100000))
# 1.0803457700021681

print(timeit.timeit('after()', globals=globals(), number=100000))
# 0.6101379450010427
