class Person:
    def __init__(self, name):
        self.name = name


def smile(person):
    print(f'{person.name} smiles')


sam = Person('Sam')
# sam.smile()
# AttributeError: 'Person' object has no attribute 'smile'

sam.smile = smile
# sam.smile()
# TypeError: smile() missing 1 required positional argument: 'person'

sam.smile(sam)  # Sam smiles

del sam.smile
Person.smile = smile
sam.smile()  # Sam smiles
