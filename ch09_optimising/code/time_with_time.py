import time
import random


def long_function(a, b):
    result = 0
    for _ in range(a):
        for _ in range(b):
            for _ in range(a):
                for _ in range(b):
                    result += random.random()
    return result


start_time = time.perf_counter_ns()
number = long_function(100, 100)
duration = time.perf_counter_ns() - start_time
print(f'Duration: {duration/10**9:.9f} seconds')
# Output:
# Duration: 4.591850348 seconds
