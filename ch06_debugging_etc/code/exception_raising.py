def validate_age(age):
    if age < 0:
        raise ValueError('Age must be positive')

    if age > 200:
        raise ValueError('Age must be 200 or less')


validate_age(300)
# ValueError: Age must be 200 or less
