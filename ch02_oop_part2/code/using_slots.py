class Vector:
    __slots__ = ('x', 'y')


vector = Vector()
vector.x = 5
vector.y = 6

vector.z = 10
# AttributeError: 'Vector' object has no attribute 'z'
