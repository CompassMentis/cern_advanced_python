import timeit


def add(a,b):
    return a + b


print(timeit.timeit(
    stmt="add(5, 10)", globals=globals(), number=10000
))
# Output:
# 0.00036350899972603656
