import time


def add_timing(function):
    def timed_function(a, b):
        start_time = time.time()
        result = function(a, b)
        duration = time.time() - start_time
        print(f'Duration {duration:.05} seconds')
        return result
    return timed_function


@add_timing
def slow_sum(a, b):
    sum = a
    while b > 0:
        b -= 10 ** -6
        sum += 10 ** -6
    return sum


print(f'{slow_sum(15, 20) = }')

# Output:
# Duration 1.0748 seconds
# slow_sum(15, 20) = 35.00000100812463
