import operator


OPERATOR_MAP = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    'x': operator.mul,
    '/': operator.truediv
}


def process_expression(expression):
    try:
        left, operand, right = expression.split()
    except ValueError:
        print('Put spaces between the numbers and the operand')
        return

    try:
        left, operand, right = float(left),OPERATOR_MAP[operand], float(right)
    except ValueError:
        print('Incorrect number(s), try again')
        return

    try:
        result = operand(left, right)
    except ZeroDivisionError:
        print("Can't divide by zero")
        return

    print(f'The answer is {result}')


expression = input('Simple sum, e.g. 5 x 2> ')
process_expression(expression)
