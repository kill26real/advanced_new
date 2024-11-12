"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
from typing import Dict
import json
import re


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    with open("skillbox_json_messages.log", "r") as file:
        information = {
            "DEBUG":0,
            "INFO":0,
            "WARNING":0,
            "ERROR":0,
            "CRITICAL":0,
        }
        for line in file:
            line = line.strip()
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                print(f"Invalid JSON: {line}")
                continue
            information[data["level"]] += 1

        return information



def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    information = {}
    with open("skillbox_json_messages.log", "r") as file:
        for line in file:
            line = line.strip()
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                print(f"Invalid JSON: {line}")
                continue
            hour = data["time"].split(":")[0]
            if not hour in information.keys():
                information[hour] = 0
            information[hour] += 1
        max_hour = max(information, key=information.get)
        return max_hour


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    logs = 0
    with open("skillbox_json_messages.log", "r") as file:
        for line in file:
            line = line.strip()
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                print(f"Invalid JSON: {line}")
                continue
            hour = data["time"].split(":")[0]
            minute = data["time"].split(":")[1]
            if str(hour) == "05" and 0 <= int(minute) <= 20 and data["level"] == "CRITICAL":
                logs += 1
        return logs

def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    logs = 0
    with open("skillbox_json_messages.log", "r") as file:
        for line in file:
            line = line.strip()
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                print(f"Invalid JSON: {line}")
                continue
            if re.search(r'\bdog\b', data['message']):
                logs += 1
        return logs


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    information = {}
    with open("skillbox_json_messages.log", "r") as file:
        for line in file:
            line = line.strip()
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                print(f"Invalid JSON: {line}")
                continue
            for word in data['message'].split(" "):
                if not word in information.keys():
                    information[word] = 0
                information[word] += 1
        max_word = max(information, key=information.get)
        return max_word


if __name__ == '__main__':
    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
