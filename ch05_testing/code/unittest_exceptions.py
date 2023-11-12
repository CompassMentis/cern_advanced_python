import unittest


def validate_age(age):
    if age < 0:
        raise ValueError('Age must be positive')

    if age > 200:
        raise ValueError('Age must be 200 or less')


class TestAgeValidation(unittest.TestCase):
    def test_too_young(self):
        with self.assertRaises(ValueError):
            validate_age(-1)

    def test_too_old(self):
        with self.assertRaises(ValueError):
            validate_age(201)

    def test_too_young_message(self):
        with self.assertRaisesRegex(ValueError, r'.*positive.*'):
            validate_age(-1)


unittest.main()
