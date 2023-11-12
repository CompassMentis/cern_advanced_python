from unittest import mock


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def validate_age(age):
        if age < 0:
            raise ValueError('Age must be positive')

        if age > 200:
            raise ValueError('Age must be 200 or less')

    def validate(self):
        try:
            self.validate_age(self.age)
        except ValueError:
            return False


def test_validate_age_failure():
    with mock.patch.object(Person, 'validate_age', new=mock.Mock()) as mock_validate_age:
        mock_validate_age.side_effect = ValueError

        person = Person('Alex', 500)
        assert person.validate() is False

# Output:
# 1 passed in 0.02s
