# Todo: Make sure you've already done ex_generator_function

# Todo: Exactly the same exercise as ex_generator_function,
#   but this time, create an iterable class called RandomNumbers
#   with the same behaviour as the random_numbers generator function

# Todo: Check your output against the expected output

import random


random.seed(21)
for number in RandomNumbers(5):
    print(number)

for a in RandomNumbers(2):
    for b in RandomNumbers(2):
        print(a, b)
# Expected output:
# 22
# 54
# 89
# 82
# 37
# 62 28
# 62 61
# 66 24
# 66 65
