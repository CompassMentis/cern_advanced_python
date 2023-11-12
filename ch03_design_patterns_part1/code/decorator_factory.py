import time


def timer_factory(repeats):
    def add_timing(function):
        def timed_function(*args, **kwargs):
            start_time = time.time()
            for _ in range(repeats):
                result = function(*args, **kwargs)
            duration = (time.time() - start_time) / repeats
            print(f'Average duration over {repeats} repeats: '
                  f'{duration:.05} seconds')
            return result
        return timed_function
    return add_timing


@timer_factory(5)
def slow_sum(a, b):
    sum = a
    while b > 0:
        b -= 10 ** -6
        sum += 10 ** -6
    return sum


print(f'{slow_sum(15, 20) = }')

# Output
# Average duration over 5 repeats: 1.0352 seconds
# slow_sum(15, 20) = 35.00000100812463
