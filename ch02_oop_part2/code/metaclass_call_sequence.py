class Logger(type):
    def __call__(self, *args, **kwargs):
        print('__call__ called')
        return super().__call__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        print('__new__ called')
        return super().__new__(cls, *args, **kwargs)


print('About to define Person')
class Person(metaclass=Logger):
    def __init__(self, name):
        self.name = name


print('About to instantiate Person')
sam = Person('Sam')

# Output, in order:

# About to define Person
# __new__ called

# About to create a Person
# __call__ called
