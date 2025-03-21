import numba
import timeit


# @numba.jit
def slow_sum(a, b):
    sum = a
    while b > 0:
        b -= 10 ** -6
        sum += 10 ** -6
    return sum


print(timeit.timeit(stmt='slow_sum(15, 20)', globals=globals(), number=3))
# Without numba: 3.1348356529997545
# With numba: 0.18508760800250457
