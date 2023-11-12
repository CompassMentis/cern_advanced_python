# Todo: Make sure you've done ex_decorator first

# Todo: Copy the decorator from your solution into this script

# Todo: Change the decorator so it supports functions with any number of arguments
#   Assume that there will only be positional arguments
#   You will need to simplify the error message - remove the name (e.g. 'a' or 'b') from it

# Todo: Add the decorator to both add_two and add_three function

def only_integers(func):
    def wrapped(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f'{arg}, not an integer')
        return func(*args)
    return wrapped


@only_integers
def add_two(a, b):
    return a + b


@only_integers
def add_three(x, y, z):
    return x + y + z

# Todo: Run the code, make sure you get the expected exception
print(add_two(1.2, 3))
# Expected output:
# TypeError: 1.2, not an integer

# Todo: Comment out the print line above, run the code again
#   and make sure you the expected exception
# print(add_three(1.6, 3, 7))
# Expected output:
# TypeError: 1.6, not an integer