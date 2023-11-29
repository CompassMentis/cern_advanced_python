import time


def add_timing(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(f'Duration {time.time() - start_time:.05} seconds')
        return result
    return wrapper


def add_entry_exit(function):
    def wrapper(*args, **kwargs):
        print(f'Entered {function.__name__}')
        result = function(*args, **kwargs)
        print(f'Exiting {function.__name__}')
        return result
    return wrapper


@add_entry_exit
@add_timing
def slow_sum(a, b):
    sum = a
    while b > 0:
        b -= 10 ** -6
        sum += 10 ** -6
    return sum


print(f'{slow_sum(15, 20) = }')

# Output:
# Entered wrapper
# Duration 1.0921 seconds
# Exiting wrapper
# slow_sum(15, 20) = 35.00000100812463
