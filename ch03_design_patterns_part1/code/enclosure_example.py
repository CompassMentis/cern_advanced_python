def outer_function(n):
    def inner_function():
        print('Outer function was called with n =', n)

    return inner_function


test_function = outer_function(5)
test_function()
