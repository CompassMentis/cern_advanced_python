import functools


numbers = [1, 2, 3, 4]

def times(a, b):
    return a * b

# Calculates 1 * 2 * 3 * 4
product = functools.reduce(times, numbers)
print(product)  # 24

# Manual version
product = numbers[0]
for number in numbers[1:]:
    product = times(product, number)

print(product)  # 24
