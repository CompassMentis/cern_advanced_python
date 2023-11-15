class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


def in_known_city(person):
    return person.city in ['London', 'Paris', 'Geneva', 'New York']

# TODO: Create a fixture which returns a Person instance

# TODO: Create a parameterised test which uses the person fixture,
#   sets the person to a known city and checks that in_known_city returns True

# TODO: Create a parameterised test which uses the person fixture,
#   sets the person to an unknown city and checks that in_known_city returns False
