import pytest


def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        # Odd number of numbers, take middle one
        return numbers[len(numbers) // 2]

    # Even number of numbers, take average of two middle ones
    return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2


@pytest.mark.parametrize('numbers, expected', [
    ([1, 2, 3, 4, 5], 3),
    ([5, 10, 15, 20, 25], 15)
])
def test_odd_number_sorted(numbers, expected):
    assert get_median(numbers) == expected

@pytest.mark.parametrize('numbers, expected', [
    ([1, 2, 3, 4, 5, 6], 3.5),
    ([5, 10, 15, 20], 12.5)
])
def test_even_number_sorted(numbers, expected):
    assert get_median(numbers) == expected

# Output:
# pytest_parameterised.py::test_odd_number_sorted[numbers0-3] PASSED       [ 25%]
# pytest_parameterised.py::test_odd_number_sorted[numbers1-15] PASSED      [ 50%]
# pytest_parameterised.py::test_even_number_sorted[numbers0-3.5] PASSED    [ 75%]
# pytest_parameterised.py::test_even_number_sorted[numbers1-12.5] PASSED   [100%]
