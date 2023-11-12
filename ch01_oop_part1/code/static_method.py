class Vector:
    @staticmethod
    def calculate_length(x, y):
        return (x ** 2 + y ** 2) ** 0.5

    def show_length(self):
        print(
            'Length',
            self.calculate_length(self.x, self.y)
        )

    def __init__(self, x, y):
        self.x = x
        self.y = y


sample_vector = Vector(10, 15)

sample_vector.show_length()
# Length 18.027756377319946