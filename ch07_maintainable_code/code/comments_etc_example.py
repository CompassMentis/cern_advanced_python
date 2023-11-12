"""
This is a doc string
It should explain what this module does
e.g.: This module is here to demonstrate docstrings and comments
"""
import re

class Demo:
    """
    Doc strings also go at the start of a class
    """
    def __init__(self, number):
        '''
        And a docstring at the start of a function (module)
        You can use single as well as double quotes - but be consistent (unlike this example code)
        function doc strings often document the parameters:
        self: class instance
        number: number of people

        and document the return value:
        returns: projected population in 10 years
        '''
        ...

a = 1   # A comment after the statement

# A comment before a statement
b = 5

# (Don't do this - just noise - doesn't add anything) A meaningless comment:
# set c to 3
c = 3

# Meaningful comment here - something which explains what this regular expression does
b = re.search('asdf', 'ABC*')


help(Demo)
