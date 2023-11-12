import time
import multiprocessing
import random
import timeit


def times_two(n):
    time.sleep(2 * random.random())
    return n * 2


class TimesTwoProcess(multiprocessing.Process):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.result = None

    def run(self):
        self.result = times_two(self.number)

### (column break)

def main():
    numbers = list(range(10))
    double_numbers = {}
    processes = []
    for number in numbers:
        process = TimesTwoProcess(number)
        process.start()
        processes.append(process)
    print('Processs started')
    for process in processes:
        process.join()
    print('Processs joined')
    for process in processes:
        double_numbers[process.number] = process.result
    print('Results in dictionary')
    print(double_numbers)
    print(sum(double_numbers.values()))


setup = 'from __main__ import main'
statement = 'main()'
print(timeit.timeit(setup=setup, stmt=statement, number=1))

# Output
# Processs joined
# Results in dictionary
# {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
