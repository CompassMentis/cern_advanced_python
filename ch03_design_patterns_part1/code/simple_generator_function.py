def numbers_generator():
    yield 5
    yield 10


numbers_iterator = numbers_generator()
print(numbers_iterator)
# <generator object numbers_generator at 0x7faaa0703480>

print(next(numbers_iterator))  # 5
print(next(numbers_iterator))  # 10
print(next(numbers_iterator))  # StopIteration
