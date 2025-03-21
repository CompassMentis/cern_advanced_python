class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def person_factory(name='Sophia', age=40):
    return Person(name, age)


test_person = person_factory()
another_test_person = person_factory(age=200)
