import timeit


def before():
    total = 0
    for i in range(100):
        for j in range(100):
            total += j * i ** 0.5
    return total


def after():
    total = 0
    for i in range(100):
        i_root = i ** 0.5
        for j in range(100):
            total += j * i_root
    return total


print(timeit.timeit('before()', globals=globals(), number=1000))
# 0.8442053269973258

print(timeit.timeit('after()', globals=globals(), number=1000))
# 0.42781283099975553
