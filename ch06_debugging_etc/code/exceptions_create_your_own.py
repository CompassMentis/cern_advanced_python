class ValidationError(Exception):
    ...


def validate_age(age):
    if age < 0:
        raise ValidationError('Age must be positive')

    if age > 200:
        raise ValidationError('Age must be 200 or less')


validate_age(300)
# ValidationError: Age must be 200 or less
