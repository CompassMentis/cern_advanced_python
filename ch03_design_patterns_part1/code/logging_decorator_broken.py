def add_logging(function):
    def wrapped(*args, **kwargs):
        print(f'Starting {function.__name__}')
        print(f'{args = }, {kwargs = }')
        result = function(*args, **kwargs)
        return result
    return wrapped


@add_logging
@add_logging
def slow_sum(a, b):
    sum = a
    while b > 0:
        b -= 10 ** -6
        sum += 10 ** -6
    return sum


print(f'{slow_sum(15, 20) = }')

# Output
# Starting wrapped
# args = (15, 20), kwargs = {}
# Starting slow_sum
# args = (15, 20), kwargs = {}
# slow_sum(15, 20) = 35.00000100812463
