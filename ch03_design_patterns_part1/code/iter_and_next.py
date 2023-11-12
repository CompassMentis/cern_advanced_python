numbers = [1, 2, 7, 15]

numbers_iterator = iter(numbers)
print(next(numbers_iterator))  # 1
print(next(numbers_iterator))  # 2
print(next(numbers_iterator))  # 7
print(next(numbers_iterator))  # 15
print(next(numbers_iterator))  # StopIteration
