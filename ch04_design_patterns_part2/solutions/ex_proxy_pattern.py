import people

# Todo: Review people.py.
#  Hint: you may want to put it side by side with this module
#  Notice how some names don't follow the Python standard (snake_case)

# Todo: Create a new Person class which is a proxy for people.Person
#   This class should have (or delegate to) the same methods, but with correct names
#   Do not copy the code from people.Person

# Todo: Run the following code and make sure it works
sam = Person(name='sam smith', city='New Delhi')
print(sam.name_in_caps)
print(sam.lives_in_capital_city)
