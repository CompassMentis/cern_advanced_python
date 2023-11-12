numbers = [1, 2, 3, 4]


def is_even(n):
    return not(n % 2)


print(list(filter(is_even, numbers)))
# [2, 4]


print([number for number in numbers if not(number % 2)])
# [2, 4]
