import timeit


def before():
    roots = []
    for i in range(10000):
        roots.append(i ** 0.5)

    return roots


def after():
    roots = [i ** 0.5 for i in range(10000)]
    return roots


print(timeit.timeit('before()', globals=globals(), number=1000))
# 0.6346115330015891

print(timeit.timeit('after()', globals=globals(), number=1000))
# 0.6020471100018767
