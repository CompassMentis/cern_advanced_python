import time


def add_timing(cls):
    def add_timing_to_method(method):
        def timed_method(*args, **kwargs):
            start_time = time.time()
            result = method(*args, **kwargs)
            duration = time.time() - start_time
            print(f'{method.__name__}, {duration:.05} seconds')
            return result
        return timed_method

    for name, item in cls.__dict__.items():
        if callable(item):
            setattr(cls, name, add_timing_to_method(item))

    return cls


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


@add_timing
class MathsFunctions:
    def __init__(self, number):
        self.number = number

    def fibonacci(self):
        return fib(self.number)


maths_functions = MathsFunctions(40)
print(maths_functions.fibonacci())


# Output:
# __init__, 7.1526e-07 seconds
# fibonacci, 7.5211 seconds
# 102334155
