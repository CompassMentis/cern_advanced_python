# Todo: create a decorator 'only_integers'
#   which wraps a function which takes two arguments, a and b
#   and checks that they are both integers
#   if any is not, it raises a TypeError, e.g.: raise TypeError(f'a = {a}, not an integer')

# Todo: Decorate add with the new decorator
def only_integers(func):
    def wrapped(a, b):
        if not isinstance(a, int):
            raise TypeError(f'a = {a}, not an integer')
        if not isinstance(b, int):
            raise TypeError(f'b = {b}, not an integer')
        return func(a, b)
    return wrapped


@only_integers
def add(a, b):
    return a + b


print(add(1, 2))
# Expected output: 3

print(add(1.2, 3))
# Expected output:
# TypeError: a = 1.2, not an integer
