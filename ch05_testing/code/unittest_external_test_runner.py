# Run with: python -m unittest unittest_external_test_runner
import unittest


def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        # Odd number of numbers, take middle one
        return numbers[len(numbers) // 2]

    # Even number of numbers, take average of two middle ones
    return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2


class Test(unittest.TestCase):
    def test_odd_number_sorted(self):
        numbers = [5, 10, 15, 20, 25]
        self.assertEquals(get_median(numbers), 15)

    def test_even_number_sorted(self):
        numbers = [1, 2, 3, 4, 5, 6]
        self.assertEquals(get_median(numbers), 3.5)


# Output:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
