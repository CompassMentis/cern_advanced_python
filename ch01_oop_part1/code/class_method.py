class Vector:
    number_of_instances = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__class__.number_of_instances += 1

    @classmethod
    def print_number_of_instances(cls):
        print(cls.number_of_instances)


vectors = [Vector(1, 2) for _ in range(5)]
vectors[0].print_number_of_instances()  # 5