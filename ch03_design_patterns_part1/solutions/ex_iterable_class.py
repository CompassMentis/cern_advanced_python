# Todo: Make sure you've already done ex_generator_function

# Todo: Exactly the same exercise as ex_generator_function,
#   but this time, create an iterable class called RandomNumbers
#   with the same behaviour as the random_numbers generator function
import random

class RandomNumbers:
    def __init__(self, n):
        self.n = n
        self.yet_to_return = n
        self.previously_drawn = set()

    def __iter__(self):
        return RandomNumbers(self.n)

    def __next__(self):
        if self.yet_to_return == 0:
            raise StopIteration

        while True:
            number = random.randint(1, 100)
            if number not in self.previously_drawn:
                break
        self.previously_drawn.add(number)
        self.yet_to_return -= 1
        return number


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

