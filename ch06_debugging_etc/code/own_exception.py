class ValidationError(Exception):
    pass


def validate_age(age):
    if age < 0:
        raise ValidationError('Age must be >= 0')
    if age > 200:
        raise ValidationError('Age must be <= 200')
