"""
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

1) email (текст, обязательно для заполнения, валидация формата);
2) phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
3) name (текст, обязательно для заполнения);
4) address (текст, обязательно для заполнения);
5) index (только числа, обязательно для заполнения);
6) comment (текст, необязательно для заполнения).
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from hw2_validators import number_length, NumberLength
from wtforms.validators import InputRequired, Email, NumberRange, ValidationError, Optional

app = Flask(__name__)

def validate_numeric(form, field):
    if not str(field.data).isdigit():
        raise ValidationError('This field must contain only numbers.')


def validate_alpha(form, field):
    if not str(field.data).isalpha():
        raise ValidationError('This field must contain only letters.')


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999), validate_numeric])
    name = StringField(validators=[InputRequired(), validate_alpha])
    address = StringField(validators=[InputRequired(), validate_alpha])
    index = IntegerField(validators=[InputRequired(), validate_numeric])
    comment = StringField(validators=[validate_alpha])


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        name, phone = form.name.data, form.phone.data

        return f"Successfully registered user {name} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
