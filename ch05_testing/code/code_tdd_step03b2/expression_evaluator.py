def parse_expression(expression):
    # Todo: better exception handling
    try:
        result = [int(expression)]
    except ValueError:
        result = [0]
    return result
