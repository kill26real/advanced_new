import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/testtt')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это тестовая страничка, ответ сгенерирован aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa в {now}'
