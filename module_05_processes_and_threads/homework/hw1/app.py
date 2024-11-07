"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""
from typing import List
import subprocess
from flask import Flask
import os
import signal
import time
app = Flask(__name__)


'COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME'
'python  2442 kirill    3u  IPv4  16305      0t0  TCP localhost:5000 (LISTEN)'


def get_pids(port: int) -> List[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError

    # result = subprocess.run(['lsof', '-i', f':{port}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True, text=True)
    output = result.stdout.strip()
    pids = []
    if output:
        lines = output.splitlines()
        if len(lines) > 1:
            for index, line in enumerate(lines):
                if index == 0:
                    continue
                pids.append(int(line.split()[1]))
            return pids
    return []


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: List[int] = get_pids(port)
    if pids:
        for pid in pids:
            os.kill(pid, signal.SIGKILL)
            time.sleep(1)


def run(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)
