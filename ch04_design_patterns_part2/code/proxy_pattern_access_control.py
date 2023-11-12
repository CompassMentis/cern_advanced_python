class MissingAccessRights(BaseException):
    ...


class Person:
    def __init__(self, name):
        self.name = name


class SecurePerson:
    def __init__(self, name, can_read, can_write):
        self.person = Person(name)
        self.can_read = can_read
        self.can_write = can_write

    @staticmethod
    def security_check(has_access):
        if not has_access:
            raise MissingAccessRights

    @property
    def name(self):
        self.security_check(self.can_read)
        return self.person.name

    @name.setter
    def name(self, new_value):
        self.security_check(self.can_write)
        self.person.name = new_value


fred = SecurePerson('Fred', can_read=True, can_write=False)
print(fred.name)         # Fred
fred.name = 'Freddie'    # MissingAccessRights
