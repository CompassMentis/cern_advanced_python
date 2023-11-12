try:
    int('five')
except Exception as e:
    print(e)
    # invalid literal for int() with base 10: 'five'

    print(e.args)
    # ("invalid literal for int() with base 10: 'five'",)

    print(repr(e))
    # ValueError("invalid literal for int() with base 10: 'five'")
