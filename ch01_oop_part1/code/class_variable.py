class Vector:
    number_of_instances_created = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__class__.number_of_instances_created += 1

        # Or do this
        # Vector.number_of_instances_created += 1


vectors = [Vector(1, 2) for _ in range(5)]
print(Vector.number_of_instances_created)  # 5
