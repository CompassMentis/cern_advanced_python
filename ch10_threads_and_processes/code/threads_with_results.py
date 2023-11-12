import time
import threading
import random
import timeit


def times_two(n):
    time.sleep(2 * random.random())
    return n * 2


class TimesTwoThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.result = times_two(self.number)

### (column break)

def main():
    numbers = list(range(10))
    double_numbers = {}
    threads = []
    for number in numbers:
        thread = TimesTwoThread(number)
        thread.start()
        threads.append(thread)
    print('Threads started')
    for thread in threads:
        thread.join()
    print('Threads joined')
    for thread in threads:
        double_numbers[thread.number] = thread.result
    print('Results in dictionary')
    print(double_numbers)
    print(sum(double_numbers.values()))


setup = 'from __main__ import main'
statement = 'main()'
print(timeit.timeit(setup=setup, stmt=statement, number=1))

# Output
# Threads started
# Threads joined
# Results in dictionary
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
# 90
# 1.9306492659961805
