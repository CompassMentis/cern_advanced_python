def times_two(x: int):
    return x * 2


print('five', times_two('five'))

# Output of 'mypy type_hints_failure.py':
# type_hints_failure.py:5: error: Argument 1 to "times_two" has incompatible type "str"; expected "int"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)

# Output of 'mypy type_hints_failure.py --strict':
# type_hints_failure.py:1: error: Function is missing a return type annotation  [no-untyped-def]
# type_hints_failure.py:5: error: Argument 1 to "times_two" has incompatible type "str"; expected "int"  [arg-type]
