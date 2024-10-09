"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys

def convert_bytes(num_bytes):
    if num_bytes < 1024:
        return f"{num_bytes} Bytes"
    elif num_bytes < 1024**2:
        return f"{num_bytes / 1024:.2f} KB"
    elif num_bytes < 1024**3:
        return f"{num_bytes / 1024**2:.2f} MB"
    elif num_bytes < 1024**4:
        return f"{num_bytes / 1024**3:.2f} GB"
    else:
        return f"{num_bytes / 1024**4:.2f} TB"

def get_mean_size(data: str) -> float:
    answer = ""

    with open(data, 'r', encoding="UTF-8") as file:
        lines = file.readlines()[2:-2]
        for line in lines:
            columns = line.split()
            format_bytes = convert_bytes(int(columns[3]))
            answer += f"Process {columns[-1]} use {format_bytes}\n"
    return answer


if __name__ == '__main__':
    data: str = sys.stdin.read()
    mean_size: float = get_mean_size(data)
    print(mean_size)
