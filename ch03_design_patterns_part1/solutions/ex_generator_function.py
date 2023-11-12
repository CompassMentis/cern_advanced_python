# Todo: Create a generator function called 'random_numbers'
#   One parameter: how_many

# Todo: (random_numbers) times it should return a random integer between 1 and 100
#   Note: Check out the 'random' module in the standard library

# Todo: It should keep track of the numbers which it already has returned
#   If it draws a number which it has already returned, it should draw another number
#   until it has drawn a new number

import random

def random_numbers(n):
    previously_drawn = set()
    for _ in range(n):
        while True:
            number = random.randint(1, 100)
            if number not in previously_drawn:
                break
        previously_drawn.add(number)
        yield number


random.seed(21)
for number in random_numbers(5):
    print(number)

# Expected output:
# 22
# 54
# 89
# 82
# 37
