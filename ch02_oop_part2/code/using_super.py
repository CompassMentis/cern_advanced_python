class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name)


lassie = Dog('Lassie', 'Rough Collie')
print(lassie.breed)  # Rough Collie
