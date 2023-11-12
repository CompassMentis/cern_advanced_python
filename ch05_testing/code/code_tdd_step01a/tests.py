# Step 1a - Broken test:
# There is a function called 'parse_expression'
# which takes a string and returns a list of strings, ints or floats

from expression_evaluator import parse_expression


def test_parse_expression_parameters():
    result = parse_expression('Hello')
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, (str, int, float))

# Output:
# E   ImportError: cannot import name 'parse_expression' from 'expression_evaluator'
