# TODO: Import deep_compare from deep_compare

# TODO: Read through the deep_compare function to get an idea of what it does

# TODO: Import pytest

# TODO: create a simple pytest test which confirms that two different integers are not the same

# TODO: create three different fixtures which all return a list
#   list_a1 and list_a2 yield lists with the same length and items
#   list_b yields a different list

# TODO: write a test for deep_compare on simple lists

# TODO: write a test for deep_compare on lists of lists

# TODO: run the tests with coverage
#  Write down the current coverage
#  Look at the coverage report and see what code isn't covered yet
#  Write a new test to increase the coverage
#  Check that the coverage has increased
from deep_compare import deep_compare

import pytest


def test_compare_single_integers():
    assert not deep_compare(10, 5)


@pytest.fixture
def list_a1():
    yield [10000, 2, 3]


@pytest.fixture
def list_a2():
    yield [10000, 2, 3]


@pytest.fixture
def list_b():
    yield [5, 7, 10]


def test_compare_equal_lists(list_a1, list_a2):
    assert deep_compare(list_a1, list_a2)
    assert deep_compare([list_a1, list_a2], [list_a1, list_a2])


def test_compare_different_lists(list_a1, list_a2, list_b):
    assert not deep_compare(list_a1, list_b)
    assert deep_compare([list_a1, list_b], [list_a2, list_b])
