import random
random.seed(0)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'


# Todo: Complete the function below, with the following behaviour:
    # if is_random
    #   Check that both x and y are false. If not, raise an AssertionError
    #   Return a Vector with both x and y a random number between 1 and 100, inclusive
    # else (if not is_random)
    #   Default for x is 5, default for y is 10
    #   Return a Vector for x and y
def vector_factory(x=None, y=None, is_random=False):


# Todo: Run the code below and make sure you get the same output
print(vector_factory())
# Vector(x=5, y=10)

print(vector_factory(1, 7))
# Vector(x=1, y=7)

print(vector_factory(is_random=True))
# Vector(x=50, y=98)  Note: you may get a different value

print(vector_factory(x=5, is_random=True))
# Raises an AssertionError
