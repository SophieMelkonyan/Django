from django.core.validators import ValidationError


def check_letters(value: str):
    if not value.isalpha():
        raise ValidationError("Title must be alphabetic")
    return value
