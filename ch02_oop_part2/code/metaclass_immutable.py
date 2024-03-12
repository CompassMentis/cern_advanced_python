class ImmutableClass(type):

    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)

        def new_set_attr(self, name, new_value):
            if name in self.__dict__:
                raise TypeError(
                    f"Cannot set attribute '{name}' of class {self.__class__.__name__}"
                )
            self.__dict__[name] = new_value

        new_cls.__setattr__ = new_set_attr

        return new_cls


class Student(metaclass=ImmutableClass):
    def __init__(self, name):
        self.name = name


amara = Student('Alex')
print(amara.name)  # Amara

# Creating new attributes still works
amara.age = 25
print(amara.age)  # 25

# Changing existing attributes fails
amara.name = 'Alexandra'
# TypeError: Cannot set attribute 'name' of class Student
