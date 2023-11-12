class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Person(metaclass=Singleton):
    def __init__(self, name):
        self.name = name


sam = Person('Sam')
fred = Person('Fred')
print(fred.name)  # Sam
print(sam is fred)  # True
