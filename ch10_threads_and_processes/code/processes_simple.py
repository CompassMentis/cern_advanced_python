import time
import multiprocessing
import random
import timeit


def times_two(n):
    time.sleep(2 * random.random())
    result = n * 2
    print(f'{n} x 2 = {result}')


def main():
    numbers = list(range(10))
    processes = []
    for number in numbers:
        process = multiprocessing.Process(target=times_two, args=(number, ))
        process.start()
        processes.append(process)
    print('Processes started')
    for thread in processes:
        thread.join()
    print('Threads joined')
    print('All done')

### (column break)

setup = 'from __main__ import main'
statement = 'main()'
print(timeit.timeit(setup=setup, stmt=statement, number=1))
# Non-threading duration, expected:
# 10 * (0..2) seconds - roughly 10 seconds
# Actual duration: 1.9670751919984468
# The slowest thread + a bit extra

# Output:
# Processes started
# 5 x 2 = 10
# 8 x 2 = 16
# 1 x 2 = 2
# 9 x 2 = 18
# 7 x 2 = 14
# 4 x 2 = 8
# 0 x 2 = 0
# 2 x 2 = 4
# 6 x 2 = 12
# 3 x 2 = 6
# Threads joined
# All done
# 1.979753141999936
