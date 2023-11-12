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
        thread.join()
        threads.append(thread)
    print('Threads joined')
    print('All done')


setup = 'from __main__ import main'
statement = 'main()'
print(timeit.timeit(setup=setup, stmt=statement, number=1))
# Non-threading duration, expected:
# 10 * (0..2) seconds - roughly 10 seconds
# Actual duration: 7.241123701998731
