import timeit

# Timing a simple statement
statement = 'a = 10; b = 50; c = a ** b'
print(statement, '|', timeit.timeit(statement))
# a = 10; b = 50; c = a ** b | 0.1964850699987437

# Timing with set up
setup = 'a = 10; b = 50'
statement = 'c = a ** b'
print(statement, '|', timeit.timeit(stmt=statement, setup=setup))
# c = a ** b | 0.19297171200014418

# Timing with import
setup = 'import math; a = 10'
statement = 'b = math.pi ** a'
print(statement, '|', timeit.timeit(stmt=statement, setup=setup))
# b = math.pi ** a | 0.04933006200008094

# Timing a local function
def fibonacci(n):
    return 1 if n <= 2 else fibonacci(n - 1) + fibonacci(n - 2)

setup = 'from __main__ import fibonacci'
statement = 'f = fibonacci(5)'
print(statement, '|', timeit.timeit(stmt=statement, setup=setup))
# f = fibonacci(5) | 0.3861391550017288
