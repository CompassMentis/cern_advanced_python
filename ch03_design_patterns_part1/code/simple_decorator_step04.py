import time


def add_timing(function):
    def timed_function(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        duration = time.time() - start_time
        print(f'Duration {duration:.05} seconds')
        return result
    return timed_function


@add_timing
def slow_sum(a, b):
    result = a
    while b > 0:
        b -= 10 ** -6
        result += 10 ** -6
    return result


@add_timing
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(f'{slow_sum(15, 20) = }')
print(f'{factorial(200) = }')

# Output (abbreviated):
# Duration 1.0904 seconds
# slow_sum(15, 20) = 35.00000100812463
# Duration 2.0504e-05 seconds
# factorial(200) = 788657867364790503552363213932185062 ......
