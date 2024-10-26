"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
import subprocess
import os

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField('Code', [validators.DataRequired()])
    timeout = IntegerField('Timeout', [validators.DataRequired(), validators.NumberRange(min=1, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    with open('temp_code.py', 'w') as f:
        f.write(code)

    command = ['python', 'temp_code.py']

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
        return f"Код выполнился успешно. Результат:\n {result.stdout}"
    except subprocess.TimeoutExpired:
        return "Время исполнения кода превысило отведенное время"
    except Exception as e:
        return f"error: {str(e)}"
    finally:
        os.remove('temp_code.py')


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm(request.form)
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data

        result = run_python_code_in_subproccess(code, timeout)
        return result
    return "not valid data"


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
