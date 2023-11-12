class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}, a {self.__class__.__name__.lower()}'


class Cat(Animal):
    ...


class Dog(Animal):
    ...


def animal_factory(animal_type, name):
    class_ = {'cat': Cat, 'dog': Dog}[animal_type]
    return class_(name)


barker = animal_factory('dog', 'Barker')
print(barker)

felix = animal_factory('cat', 'Felix')
print(felix)
