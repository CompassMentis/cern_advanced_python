def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        # Odd number of numbers, take middle one
        return numbers[len(numbers) // 2]

    # Even number of numbers, take average of two middle ones
    return (numbers[len(numbers) // 2 + 1] + numbers[len(numbers) // 2]) / 2


def test_odd_number_sorted():
    numbers = [5, 10, 15, 20, 25]
    assert get_median(numbers) == 15


def test_even_number_sorted():
    numbers = [1, 2, 3, 4, 5, 6]
    assert get_median(numbers) == 3.5

# Output:
# pytest_broken.py:15 (test_even_number_sorted)
# 4.5 != 3.5
#
# Expected :3.5
# Actual   :4.5
