try:
    int('five')
except Exception as exception:
    print(exception)
    # invalid literal for int() with base 10: 'five'

    print(exception.args)
    # ("invalid literal for int() with base 10: 'five'",)

    print(repr(exception))
    # ValueError("invalid literal for int() with base 10: 'five'")
