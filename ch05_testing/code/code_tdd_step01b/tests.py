from expression_evaluator import parse_expression


def test_parse_expression_parameters():
    result = parse_expression('Hello')
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, (str, int, float))

# Output:
# 1 passed in 0.00s
