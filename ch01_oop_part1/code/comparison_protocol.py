class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


vector_a = Vector(3, 2)
vector_b = Vector(3, 2)
vector_c = Vector(5, 5)
print(vector_a == vector_b)   # True
print(vector_a == vector_c)   # False


