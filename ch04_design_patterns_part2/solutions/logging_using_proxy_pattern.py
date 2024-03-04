# Part 1 - Factory Pattern
# Done: Create a function, e.g. vector_factory, which takes an x and y value
#  and returns an instance of the Vector class

# Done: Instead of creating instances of the Vector class directly,
#   use the new factory function instead

# Done: Run the code and make sure it still gives the expected output

# Part 2 - Proxy Pattern
# Todo: Create LoggingVector, as proxy for the Vector class
#   It must have the same signature (method headers) as the Vector class
#   Print out each method call. For instance: "__init__(2, 7)"
#   But make the Vector class' methods do the real work
#   hint: use super(). to access them

# Todo: Change the vector_factory function so it returns LoggingVector instances instead

# Todo: Run the code, check that you get the original output plus the logged output

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector_factory(
            self.x + other.x,
            self.y + other.y
        )

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


class LoggingVector(Vector):
    def __init__(self, x, y):
        print(f'LoggingVector.__init__({x}, {y})')
        super().__init__(x, y)

    def __add__(self, other):
        print(f'LoggingVector.__add__({self}, {other})')
        return super().__add__(other)


def vector_factory(x, y):
    return LoggingVector(x, y)

vector_a = vector_factory(3, 2)
vector_b = vector_factory(5, 7)
vector_c = vector_a + vector_b
print(vector_c.x)   # 8
