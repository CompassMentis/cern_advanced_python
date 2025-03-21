import unittest


def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        # Odd number of numbers, take middle one
        return numbers[len(numbers) // 2]

    # Even number of numbers, take average of two middle ones
    return (numbers[len(numbers) // 2 + 1] + numbers[len(numbers) // 2]) / 2


class Test(unittest.TestCase):
    def test_odd_number_sorted(self):
        numbers = [5, 10, 15, 20, 25]
        self.assertEqual(get_median(numbers), 15)

    def test_even_number_sorted(self):
        numbers = [1, 2, 3, 4, 5, 6]
        self.assertEqual(get_median(numbers), 3.5)


unittest.main()

# Output:
# F.
# ======================================================================
# FAIL: test_even_number_sorted (__main__.Test.test_even_number_sorted)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "unittest_broken.py", line 21, in test_even_number_sorted
#     self.assertEquals(get_median(numbers), 3.5)
# AssertionError: 4.5 != 3.5
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# FAILED (failures=1)
