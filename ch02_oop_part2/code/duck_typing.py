class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector(
            self.x * other,
            self.y * other
        )

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


print('Hello' * 2)  # HelloHello
print(5 * 2)  # 10
print([1, 2, 3] * 2)  # [1, 2, 3, 1, 2, 3]
print(Vector(3, 2) * 2)  # Vector(6, 4)
