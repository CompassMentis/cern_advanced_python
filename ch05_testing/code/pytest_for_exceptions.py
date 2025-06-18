import pytest

def validate_age(age):
    if age < 0:
        raise ValueError('Age must be positive')
    if age > 500:
        raise ValueError('Age must be 500 or less')


def test_validate_age():
    with pytest.raises(ValueError, match='must be positive'):
        validate_age(-5)

    with pytest.raises(ValueError):
        validate_age(700)
