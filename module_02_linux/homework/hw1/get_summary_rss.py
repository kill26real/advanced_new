"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""
import os
import chardet


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

def get_summary_rss(output_file) -> str:
    answer = ""
    with open(output_file, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open(output_file, 'r', encoding=encoding) as file:
        lines = file.readlines()[2:-2]
        for line in lines:
            columns = line.split()
            format_bytes = convert_bytes(int(columns[5]))
            answer += f"Process {columns[-1]} use {format_bytes}\n"
    return answer


if __name__ == '__main__':
    cwd = os.getcwd()
    path: str = os.path.dirname(cwd) + '/output_file.txt'
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
