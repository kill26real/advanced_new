"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""

from flask import Flask, request, jsonify
import subprocess
import shlex
app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args = request.args.getlist('arg')
    arguments = [shlex.quote(s) for s in args]
    cmd = ['ps'] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f'output: {result.stdout}'
    except subprocess.CalledProcessError as e:
        return f'error: {str(e)}'


if __name__ == "__main__":
    app.run(debug=True)
