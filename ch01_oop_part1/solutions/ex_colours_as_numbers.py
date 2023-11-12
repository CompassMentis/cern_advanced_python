# Todo: Create a new class 'Colour'

# Todo: The constructor takes a single 'name' parameter
#   ... just store it as an attribute

# Todo: The __str__ method just returns the .name

# Todo: When you add two instances of Colour together,
#   it creates a new Colour instance,
#   which is a mix of the two original colours
#   Only support the following colour mixes:
#   - red + blue = purple
#   - blue + yellow = green
#   - red + yellow = orange

class Colour:
    colour_combinations = {
        ('blue', 'red') : 'purple',
        ('blue', 'yellow'): 'green',
        ('red', 'yellow'): 'orange'
    }

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        if self == other:
            return Colour(self.name)
        names = tuple(sorted((self.name, other.name)))
        return Colour(self.colour_combinations[names])

    def __str__(self):
        return self.name


red = Colour('red')
blue = Colour('blue')
print(red + blue)
# Expected output: purple

# Todo: Also test red + yellow
yellow = Colour('yellow')
print(red + yellow)

# Todo (bonus): When adding two of the same colour, return the original colour
print(red + red)
# Expected output: red

# Todo (bonus): Also support '==' comparison, based on the colour name
#     For instance 'red == blue' should return False
print(red == blue)
