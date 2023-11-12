import time
import threading
import random
import timeit


def times_two(n):
    time.sleep(2 * random.random())
    result = n * 2
    print(f'{n} x 2 = {result}')


def main():
    numbers = list(range(10))
    threads = []
    for number in numbers:
        thread = threading.Thread(target=times_two, args=(number, ))
        thread.start()
        threads.append(thread)
    print('Threads started')
    for thread in threads:
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
# Threads started
# 3 x 2 = 6
# 5 x 2 = 10
# 2 x 2 = 4
# 1 x 2 = 2
# 9 x 2 = 18
# 7 x 2 = 14
# 8 x 2 = 16
# 0 x 2 = 0
# 4 x 2 = 8
# 6 x 2 = 12
# Threads joined
# All done
# 1.9670751919984468
