# Run with
# pytest --cov=pytest_missing_coverage pytest_missing_coverage.py --cov-report=html
import pytest


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b


@pytest.fixture
def calculator():
    yield Calculator()


def test_add(calculator):
    result = calculator.add(2, 3)
    assert result == 5


def test_subtract(calculator):
    result = calculator.subtract(5, 3)
    assert result == 2

# Output, abbreviated:
# 2 passed in 0.01s
