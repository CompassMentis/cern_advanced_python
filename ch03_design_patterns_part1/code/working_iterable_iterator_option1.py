import random


class NumbersIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        result = self.numbers[self.index]
        self.index += 1
        return result


class RandomNumbers:
    def __init__(self, how_many):
        self.numbers = [random.randint(1, 100) for _ in range(how_many)]
        print('Numbers generated', self.numbers)

    def __iter__(self):
        return NumbersIterator(self.numbers)


three_random_numbers = RandomNumbers(3)
for a in three_random_numbers:
    for b in three_random_numbers:
        print(a, b)
