class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector, x={self.x}, y={self.y}'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


class Dummy:
    ...


sample_vector = Vector(10, 15)

print(sample_vector)  # Vector, x=10, y=15

print(repr(sample_vector))  # Vector(10, 15)

sample_dummy = Dummy()
print(sample_dummy)
# <__main__.Dummy object at 0x7fdc0b3e0f90>
