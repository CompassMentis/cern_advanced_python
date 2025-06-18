import time


def slow_sum(a, b):
    start_time = time.time()
    result = a
    while b > 0:
        b -= 10 ** -6
        result += 10 ** -6
    duration = time.time() - start_time
    print(f'Duration {duration:.05} seconds')
    return result


print(f'{slow_sum(15, 20) = }')

# Output:
# Duration 1.0481 seconds
# slow_sum(15, 20) = 35.00000100812463
