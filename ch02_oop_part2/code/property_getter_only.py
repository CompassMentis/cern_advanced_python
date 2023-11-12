import datetime


class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def year_of_birth(self):
        return self.date_of_birth.year


person = Person('Sam', datetime.date(1975, 10, 23))
print(person.year_of_birth)   # 1975
