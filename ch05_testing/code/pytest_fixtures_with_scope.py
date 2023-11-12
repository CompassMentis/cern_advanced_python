import pytest


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


@pytest.fixture(scope='module')
def calculator():
    print('Set up - Creating a calculator instance')
    result = Calculator()

    yield result

    print('Tear down - Destroying the calculator instance')
    # Note: happens automatically when the function finishes
    # and 'result' goes out of scope


def test_add(calculator):
    result = calculator.add(2, 3)
    assert result == 5


def test_subtract(calculator):
    result = calculator.subtract(5, 3)
    assert result == 2

# Output, abbreviated, line breaks added for readability:
# pytest_fixtures_with_scope.py::test_add
# Set up - Creating a calculator instance
# PASSED                           [ 50%]
# pytest_fixtures_with_scope.py::test_subtract PASSED                      [100%]
# Tear down - Destroying the calculator instance
