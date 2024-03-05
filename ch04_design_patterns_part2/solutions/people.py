# Used in ex_proxy_pattern.py

class Person:
    def __init__(self, Name, City):
        self.Name = Name
        self.City = City

    @property
    def lives_in_capital_city(self):
        return self.Name in ['New Delhi', 'Amsterdam', 'London', 'Paris']

    @property
    def nameInCaps(self):
        return self.Name.title()
