class Pet:
    def __init__(self, name):
        self.name = name

    def stroke(self):
        print(f'{self.name} is happy')


class Dog(Pet):
    def bark(self):
        print(f'{self.name} barks')


felix = Pet('Felix')  # Felix is happy
felix.stroke()

lassie = Dog('Lassie')  # Lassie barks
lassie.bark()

felix.bark()
# AttributeError: 'Pet' object has no attribute 'bark'
