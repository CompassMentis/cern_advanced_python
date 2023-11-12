class Person:
    def __init__(self, name):
        self.__dict__['_name'] = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value

    def __setattr__(self, key, new_value):
        if key.startswith('_'):
            raise NotImplementedError
        self.__dict__['_name'] = new_value


person = Person('Alex')
person.name = 'Alexandra'
print(person.name)  # Alexandra
person._name = 'Alex'  # NotImplemented

