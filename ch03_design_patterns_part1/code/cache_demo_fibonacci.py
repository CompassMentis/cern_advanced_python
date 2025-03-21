import functools
import timeit


@functools.lru_cache()
def fib(n):
    global call_count
    call_count += 1
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


call_count = 0
print(timeit.timeit(stmt='fib(30)', globals=globals(), number=10))
print(call_count)

# With decorator: 1.1860000086016953e-05 seconds, 30 calls
# Without decorator: 0.6756123399973148 seconds, 16640790 calls
