import itertools

import pytest

from ex_functions_to_test import find_primes_in_range
from ex_functions_to_test import remove_duplicates_preserve_order


class TestFindPrimesInRange:
    """
    Tests for find_primes_in_range
    - end < start: returns nothing
    - 1 is not a prime
    - 1 - 10 should return 2, 3, 5, 7
    """
    @pytest.mark.parametrize(
        'start, end',
        [
            (0, 0),
            (10, 10),
            (5, 3),
            (100, 98)
        ]
    )
    def test_empty_range(self, start, end):
        assert find_primes_in_range(start, end) == []

    @pytest.mark.parametrize(
        'start, end, primes_in_range',
        [
            (0, 10, [2, 3, 5, 7]),
            (2, 5, [2, 3, 5]),
        ]
    )
    def one_is_not_a_prime(self, start, end, primes_in_range):
        assert find_primes_in_range(start, end) == primes_in_range

    def test_know_list_of_primes(self):
        assert find_primes_in_range(1, 10) == [2, 3, 5, 7]


class TestRemoveDuplicatesPreserveOrder:
    """
    Tests for remove_duplicates_preserve_order
    - All unique, returns original
    - Removes duplicates
    - Retains order
    """
    def test_returns_original_if_all_unique(self):
        assert remove_duplicates_preserve_order([1, 2, 7, 3]) == [1, 2, 7, 3]

    def test_removes_duplicates(self):
        assert remove_duplicates_preserve_order([1, 1, 2, 7, 2, 3]) == [1, 2, 7, 3]

    def test_retains_order(self):
        for lst in itertools.permutations([1, 2, 7, 3, 5]):
            lst = list(lst)
            assert remove_duplicates_preserve_order(lst) == lst
