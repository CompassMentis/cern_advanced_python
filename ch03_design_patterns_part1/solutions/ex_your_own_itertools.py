# Todo: Examine one or two of the itertool functions,
#   and rewrite it yourself as a generator function or generator expression

# Todo: Write some code which compares your version and the original one,
#   to make sure they produce the same result
import itertools


def count(start, step=1):
    while True:
        yield start
        start += step


def cycle(iterator):
    while True:
        yield from iterator


def repeat(value, times=None):
    if times:
        for _ in range(times):
            yield value
    else:
        while True:
            yield value


def compare(my_version, itertools_version, args):
    my_results = list(itertools.islice(my_version(*args), 10))
    itertools_result = list(itertools.islice(itertools_version(*args), 10))
    print(my_version.__name__, args)
    print(my_results)
    print(itertools_result)
    assert my_results == itertools_result


compare(count, itertools.count, (7, ))
compare(cycle, itertools.cycle, ('abc', ))
compare(repeat, itertools.repeat, (5, ))
compare(repeat, itertools.repeat, (5, 8))
