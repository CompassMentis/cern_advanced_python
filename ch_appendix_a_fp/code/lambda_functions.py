names = ['Maura', 'Nicolas', 'Reggie', 'Rex', 'Leonel']

# Sort on length
print(sorted(names, key=len))
# ['Rex', 'Maura', 'Reggie', 'Leonel', 'Nicolas']

# Sort on last character
print(sorted(names, key=lambda name: name[-1]))
# ['Maura', 'Reggie', 'Leonel', 'Nicolas', 'Rex']

# Don't do this - using lambda to create a named function
plus_one = lambda x: x + 1

# Do this instead - use def
def plus_one(x):
    return x + 1
