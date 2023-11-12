class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )


vector_a = Vector(3, 2)
vector_b = Vector(5, 7)
vector_c = vector_a + vector_b
print(vector_c.x)   # 8
