"""
Напишите GET-эндпоинт /uptime, который в ответ на запрос будет выводить строку вида f"Current uptime is {UPTIME}",
где UPTIME — uptime системы (показатель того, как долго текущая система не перезагружалась).

Сделать это можно с помощью команды uptime.
"""

from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_str = str(datetime.timedelta(seconds=uptime_seconds)).split('.')[0]
    return f'Current uptime is {uptime_str}'


if __name__ == '__main__':
    app.run(debug=True)
