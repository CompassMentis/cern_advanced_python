class Combine:
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def __getitem__(self, item):
        return self.list_a[item] + self.list_b[item]


all_ones = [1, 1, 1, 1, 1]
numbers = [2, 3, 5, 8, 9]
combined = Combine(all_ones, numbers)
print(combined[2])   # 1 + 5 = 6
