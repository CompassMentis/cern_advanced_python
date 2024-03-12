import random


class InfiniteDiceRoll:
    def __init__(self):
        self._rolls = {}

    def __getitem__(self, item):
        if item not in self._rolls:
            self._rolls[item] = random.randint(1, 6)
        return self._rolls[item]


rolls = InfiniteDiceRoll()

for number in [1, 5, 10, 1_000_000, 10, 1_000_000]:
    print(number, rolls[number])
