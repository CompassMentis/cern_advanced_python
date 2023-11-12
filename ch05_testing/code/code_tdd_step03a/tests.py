# Step 3a - Broken test:
# parse_expression can parse sequences of digits into integers

import pytest
from expression_evaluator import parse_expression


@pytest.mark.parametrize('string, expected', [
    ('124', [124]), ('35', [35])
])
def test_parse_expression_digits(string, expected):
    assert parse_expression(string) == expected


def test_parse_expression_operators():
    result = parse_expression('Hello')
    for item in result:
        if isinstance(item, str):
            assert item in '+-*/'


def test_parse_expression_parameters():
    result = parse_expression('Hello')
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, (str, int, float))


# Output (abridged):
# ['+', '-', 5, 2.1] != [124]
# ['+', '-', 5, 2.1] != [35]
