# Todo: The __init__ method creates a _age attribute and sets it to None

# Todo: Create an age property getter which returns _age

# Todo: Create an age property setter which rounds the age down to the nearest integer
#   and then stores it in _age

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = None
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_value):
        self._age = int(new_value)


alex = Person('Alex', 23.2)
print(alex.age)

alex.age = 33.5
print(alex.age)

# Expected output:
# 23
# 33
