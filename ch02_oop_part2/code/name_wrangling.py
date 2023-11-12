class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value


person = Person('Sam')
print(person.name)  # Sam

print(person._Person__name)  # Sam

print(person.__name)
# AttributeError: 'Person' object has no attribute '__name'.
