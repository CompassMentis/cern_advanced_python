import pytest


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

@pytest.fixture
def person():
    yield Person('Sophie', 50, 'Oslo')


class TestInKnownCity:
    @pytest.mark.parametrize('city', ['London', 'Paris'])
    def test_is_known(self, city, person):
        person.city = city
        assert in_known_city(person)

    @pytest.mark.parametrize('city', ['Bristol', 'Den Haag', 'Scheveningen'])
    def test_is_not_known(self, city, person):
        person.city = city
        assert not in_known_city(person)
