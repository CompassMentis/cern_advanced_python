import time
import functools


@functools.lru_cache
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


start_time = time.time()
print(f'{fibonacci(40) = }')
duration = time.time() - start_time
print(f'{duration = }')

# Output, without decorator:
# fibonacci(40) = 102334155
# duration = 7.836722135543823

# Output, with decorator:
# fibonacci(40) = 102334155
# duration = 1.9073486328125e-05
