import dataclasses
import pytest

@dataclasses.dataclass
class Person:
    name: str
    postcode: str
    social_security_number: str

    def post__init__(self):
        assert self.is_valid()

    def is_valid(self):
        return len(self.name) > 5 and \
            ' ' in self.postcode and \
            len(self.postcode) == 7 and \
            int(self.social_security_number) % 19 == 3 and \
            len(self.social_security_number) == 12

    def get_credit_rating(self):
        # To do: Some complicated code here please
        return 0.83


@pytest.fixture
def person():
    return Person('Alex', 'AB1 2CD', '340923809869')


def test_get_credit_rating(person):
    assert person.get_credit_rating() == 0.83
