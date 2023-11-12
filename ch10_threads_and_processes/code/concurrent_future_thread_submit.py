from concurrent import futures
import time
import random
import timeit


def times_two(n):
    time.sleep(2 * random.random())
    return n * 2


def main():
    numbers = list(range(10))
    executor = futures.ThreadPoolExecutor(max_workers=1000)
    result_futures = []
    for number in numbers:
        result_futures.append(
            executor.submit(times_two, number)
        )
    print('Jobs submitted')

    total = 0
    for result_future in result_futures:
        total += result_future.result()

    print('Jobs done')
    print(total)


setup = 'from __main__ import main'
statement = 'main()'
print(timeit.timeit(setup=setup, stmt=statement, number=1))

# Output
# Jobs submitted
# Jobs done
# 90
# 1.915700169000047
