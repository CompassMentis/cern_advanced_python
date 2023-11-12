class Vector:
    def __init__(self, x, y):
        self._values = [x, y]

    def __getattr__(self, item):
        if item == 'x':
            return self._values[0]

        if item == 'y':
            return self._values[1]

        raise AttributeError


sample_vector = Vector(10, 15)

print(sample_vector.x)  # 10
