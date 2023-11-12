import pytest


def validate_age(age):
    if age < 0:
        raise ValueError('Age must be positive')

    if age > 200:
        raise ValueError('Age must be 200 or less')


def test_too_young():
    with pytest.raises(ValueError):
        validate_age(-1)


def test_too_old():
    with pytest.raises(ValueError):
        validate_age(201)


def test_too_young_message():
    with pytest.raises(ValueError, match=r'.*positive.*'):
        validate_age(-1)


# Output:
# ============================= test session starts ==============================
# collecting ... collected 3 items
#
# pytest_exceptions.py::test_too_young PASSED                              [ 33%]
# pytest_exceptions.py::test_too_old PASSED                                [ 66%]
# pytest_exceptions.py::test_too_young_message PASSED                      [100%]
#
# ============================== 3 passed in 0.01s ===============================
