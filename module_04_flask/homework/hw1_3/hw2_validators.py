"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms.validators import ValidationError
from wtforms import Field


def number_length(min: int, max: int, message: Optional[str] = None):
    # message = 'Phone must be between 1000000000 and 9999999999 characters long.'
    if not max > min or max > 9999999999 or min < 1000000000:
        raise ValidationError('This field must be in format [9999999999].')


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        if not message:
            message = 'Phone must be between 1000000000 and 9999999999 characters long.'
        self.message = message

    def __call__(self, form, field):
        if not self.max > self.min or self.max > 9999999999 or self.min < 1000000000:
            raise ValidationError(self.message)

