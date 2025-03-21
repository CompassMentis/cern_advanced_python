a = 5
b = 0
numbers = [1, 2, 3, 4]

try:
    numbers[2] = a / b
except ValueError:
    print('Some ValueError')
except IndexError:
    print('An IndexError')
except Exception as exception:
    print('Another exception:', repr(exception))
    print('With args:', exception.args)
else:
    print('All fine, no exception')
finally:
    print('Just tidying up')

# Output
# Another exception: ZeroDivisionError('division by zero')
# With args: ('division by zero',)
# Just tidying up

