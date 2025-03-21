import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
        self.assertNotEqual('hello'.upper(), 'Hello')


class TestFloatingPointOperations(unittest.TestCase):
    def test_sum(self):
        self.assertAlmostEqual(0.1 + 0.1 + 0.1, 0.3)
        self.assertNotEqual(0.1 + 0.1 + 0.1, 0.3)


class TestSets(unittest.TestCase):
    def test_add_remove(self):
        numbers = {1, 2, 3}
        self.assertIn(2, numbers)

        numbers.add(12)
        self.assertIn(12, numbers)
        self.assertNotIn(15, numbers)

        numbers.remove(3)
        self.assertNotIn(3, numbers)


unittest.main()
# Ran 3 tests in 0.000s
#
# OK
