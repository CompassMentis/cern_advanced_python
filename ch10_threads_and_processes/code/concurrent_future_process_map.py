from concurrent import futures
import time
import random
import timeit


def times_two(n):
    time.sleep(2 * random.random())
    return n * 2


def main():
    numbers = list(range(10))
    executor = futures.ProcessPoolExecutor()

    # Long version - similar to .submit example
    # total = 0
    # for result in executor.map(times_two, numbers):
    #     total += result

    # Even shorter version:
    total = sum(executor.map(times_two, numbers))

    print('Jobs done')
    print(total)


setup = 'from __main__ import main'
statement = 'main()'
print(timeit.timeit(setup=setup, stmt=statement, number=1))

# Output
# Jobs done
# 90
# 1.971637951000048
