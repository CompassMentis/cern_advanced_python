
# Todo: Create a function: create_vector_class(name, can_add=False)
#   Which returns a class with the given name
#   If can_add is True, then it should be exactly the same as the Vector class below
#   If it is False, the new class should not have the __add__ method

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return __class__(
#             self.x + other.x,
#             self.y + other.y
#         )
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.x}, {self.y})'

def create_vector_class(name, can_add=False):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.__class__(
            self.x + other.x,
            self.y + other.y
        )

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    dct = {
        '__init__': __init__,
        '__repr__': __repr__,
    }

    if can_add:
        dct['__add__'] = __add__

    return type(name, (), dct)


VectorCanAdd = create_vector_class('VectorCanAdd', can_add=True)
vector_a = VectorCanAdd(5, 3)
vector_b = VectorCanAdd(6, 9)
print(vector_a + vector_b)
# Expected output: VectorCanAdd(11, 12)

VectorCannotAdd = create_vector_class('VectorCanCompare', can_add=False)
vector_a = VectorCannotAdd(5, 3)
vector_b = VectorCannotAdd(6, 9)
print(vector_a + vector_b)
# Expected output: TypeError: unsupported operand type(s) for +: 'VectorCanCompare' and 'VectorCanCompare'