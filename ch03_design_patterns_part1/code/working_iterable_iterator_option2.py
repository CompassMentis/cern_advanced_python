import random


class RandomNumbers:
    def __init__(self, how_many=None, numbers_drawn=None):
        if how_many is not None:
            self.numbers = [random.randint(1, 100) for _ in range(how_many)]
            print('Numbers generated', self.numbers)
        else:
            self.numbers = numbers_drawn
        self.index = 0

    def __iter__(self):
        return RandomNumbers(numbers_drawn=self.numbers)

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        result = self.numbers[self.index]
        self.index += 1
        return result


three_random_numbers = RandomNumbers(3)
for a in three_random_numbers:
    for b in three_random_numbers:
        print(a, b)
