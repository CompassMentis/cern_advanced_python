class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self, factor):
        self.x *= factor
        self.y *= factor


sample_vector = Vector(10, 15)
print(sample_vector.x)  # 10

sample_vector.multiply(2)
print(sample_vector.x)  # 20
