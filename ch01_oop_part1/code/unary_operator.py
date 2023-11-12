class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Vector(-self.x, -self.y)


vector_a = Vector(3, 2)
vector_b = -vector_a
print(vector_b.x)   # -3
