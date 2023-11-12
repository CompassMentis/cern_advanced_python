from expression_evaluator import parse_expression


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


# Output:
# 2 passed in 0.01s
