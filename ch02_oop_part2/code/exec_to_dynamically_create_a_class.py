def data_class_definition(class_name, attribute_names):
    init_lines = ''.join(
        f'        self.{name} = name\n'
        for name in attribute_names
    )
    definition = f"""
class {class_name}:
    def __init__(self, {', '.join(attribute_names)}):
{init_lines}
"""

    return definition


attributes = 'name', 'age'
class_definition = data_class_definition('Person', attributes)
print(class_definition)
exec(class_definition)

person = Person('Amara', 55)
print(f'{person.name = }')
print(f'{person.age = }')
