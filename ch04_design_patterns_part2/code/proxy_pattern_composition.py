class Calculator:
    def add(self, a, b):
        print('add called:', end=' ')
        return a + b

    def sub(self, a, b):
        print('sub called:', end=' ')
        return a - b


class CachedCalculator:
    def __init__(self):
        self.cache = {}
        self.calculator = Calculator()

    def add_caching(self, func, a, b):
        key = func.__name__, a, b
        if key not in self.cache:
            self.cache[key] = func(a, b)
        return self.cache[key]

    def add(self, a, b):
        return self.add_caching(self.calculator.add, a, b)

    def sub(self, a, b):
        return self.add_caching(self.calculator.sub, a, b)


calculator = CachedCalculator()
print(calculator.add(5, 10))
print(calculator.add(5, 10))
print(calculator.sub(5, 10))
print(calculator.cache)
