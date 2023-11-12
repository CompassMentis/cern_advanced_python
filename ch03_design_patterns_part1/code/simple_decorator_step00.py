import time


def slow_sum(a, b):
    start_time = time.time()
    sum = a
    while b > 0:
        b -= 10 ** -6
        sum += 10 ** -6
    duration = time.time() - start_time
    print(f'Duration {duration:.05} seconds')
    return sum


print(f'{slow_sum(15, 20) = }')

# Output:
# Duration 1.0481 seconds
# slow_sum(15, 20) = 35.00000100812463
