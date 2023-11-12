import timeit

numbers = range(10_000_000)

list_of_squares = [number ** 2 for number in numbers]
print(timeit.timeit(
    'list_of_squares = [number ** 2 for number in numbers]',
    globals=globals(),
    number=1
))  # 0.48837746099889046

squares_generator = (number ** 2 for number in numbers)
print(timeit.timeit(
    'squares_generator = (number ** 2 for number in numbers)',
    globals=globals(),
    number=1
))  # 1.1000010999850929e-06

# print(len(squares_generator))
# TypeError: object of type 'generator' has no len()

list_of_squares_iterator = iter(list_of_squares)
for _ in range(4):
    print(next(list_of_squares_iterator), end=',')
    print(next(squares_generator))

# Output:
# 0,0
# 1,1
# 4,4
# 9,9
