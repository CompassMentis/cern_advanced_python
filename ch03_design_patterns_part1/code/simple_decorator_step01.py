import time


def slow_sum(a, b):
    sum = a
    while b > 0:
        b -= 10 ** -6
        sum += 10 ** -6
    return sum


def time_function(function, a, b):
    start_time = time.time()
    result = function(a, b)
    duration = time.time() - start_time
    print(f'Duration {duration:.05} seconds')
    return result


print(f'{time_function(slow_sum, 15, 20) = }')

# Output:
# Duration 1.0637 seconds
# time_function(slow_sum, 15, 20) = 35.00000100812463
