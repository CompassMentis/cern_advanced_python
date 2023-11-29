def times_two(x):
    return x * 2


print(5, times_two(5))

# Output of 'mypy type_hints_before.py':
# Success: no issues found in 1 source file

# Output of 'mypy type_hints_before.py --strict':
# type_hints_before.py:1: error: Function is missing a type annotation  [no-untyped-def]
# type_hints_before.py:5: error: Call to untyped function "times_two" in typed context  [no-untyped-call]
# Found 2 errors in 1 file (checked 1 source file)
