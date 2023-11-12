def __init__(instance, x, y):
    instance.x = x
    instance.y = y


def __repr__(instance):
    return f'Vector ({instance.x}, {instance.y})'


attributes = {
    '__init__': __init__,
    '__repr__': __repr__,
    'dimensions': 2
}

Vector = type('Vector', (), attributes)

vector_a = Vector(2, 3)
print(vector_a)  # Vector (2, 3)
print(vector_a.dimensions)  # 2
