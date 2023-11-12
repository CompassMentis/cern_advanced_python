numbers = [1, 2, 3, 4]

def squared(n):
    return n ** 2


print(list(map(squared, numbers)))
# [1, 4, 9, 16]


print([number ** 2 for number in numbers])
# [1, 4, 9, 16]
