import time
from unittest import mock


def slow_function():
    time.sleep(3)
    return 5


def complex_calculation():
    return slow_function() * 3


def test_complex_calculation():
    global slow_function
    slow_function = mock.Mock()
    slow_function.return_value = 5
    assert complex_calculation() == 15

# Output:
# 1 passed in 0.02s
