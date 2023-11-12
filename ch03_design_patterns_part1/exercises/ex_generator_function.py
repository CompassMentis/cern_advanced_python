# Todo: Create a generator function called 'random_numbers'
#   One parameter: how_many

# Todo: (random_numbers) times it should return a random integer between 1 and 100
#   Note: Check out the 'random' module in the standard library

# Todo: It should keep track of the numbers which it already has returned
#   If it draws a number which it has already returned, it should draw another number
#   until it has drawn a new number

import random

# Note: We're using a fixed seed for the random generator
#   so that everyone will have the same sequence of numbers
#   and so that one number will come up twice
random.seed(21)
for number in random_numbers(5):
    print(number)

# Todo: Check your output against the expected output
# Expected output:
# 22
# 54
# 89
# 82
# 37
