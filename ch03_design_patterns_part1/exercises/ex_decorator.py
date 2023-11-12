# Todo: create a decorator 'only_integers'
#   which wraps a function which takes two arguments, a and b
#   and checks that they are both integers
#   if any is not, it raises a TypeError, e.g.: raise TypeError(f'a = {a}, not an integer')

# Todo: Decorate add with the new decorator

def add(a, b):
    return a + b


print(add(1, 2))
# Expected output: 3

print(add(1.2, 3))
# Expected output:
# TypeError: a = 1.2, not an integer
