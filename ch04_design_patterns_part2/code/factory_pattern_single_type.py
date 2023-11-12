# Incomplete code

class Person:
    ...


class SecurePerson:
    ...


def person_factory(name):
    # Current version, after adding in security
    return SecurePerson(name)

    # Previous version, before adding in security
    # return Person(name)


fred = person_factory('Fred')
