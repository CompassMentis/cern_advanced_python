import dataclasses


@dataclasses.dataclass
class Person:
    name: str
    age: int
    city: str


fred = Person('Fred', 33, 'Paris')

print(fred.name)
# Fred

print(fred)
# Person(name='Fred', age=33, city='Paris')
