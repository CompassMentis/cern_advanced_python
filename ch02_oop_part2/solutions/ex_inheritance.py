# Here are four different classes
# Todo: Use inheritance to remove the duplicate code

# Todo: When done, check that the output hasn't changed
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def bark(self):
        print(f'{self.name} barks')


class SheepDog(Dog):
    def bark(self):
        print(f'{self.name} barks gently')

    def rounds_up_sheep(self):
        print(f'Sheepdog {self.name} rounds up some sheep')


class Cat(Animal):
    def miaow(self):
        print(f'{self.name} miaows')


felix = Cat('Felix')
felix.miaow()
# Output:

moggy = Dog('Moggy')
moggy.bark()

hunter = SheepDog('Hunter')
hunter.bark()
hunter.rounds_up_sheep()

# Expected output:
# Felix miaows
# Moggy barks
# Hunter barks gently
# Sheepdog Hunter rounds up some sheep
