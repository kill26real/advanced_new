"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask
from datetime import datetime

app = Flask(__name__)

global storage
storage = {}


@app.route("/add/<date>/<number>")
def add(date: str, number: int):
    if not str(number).isdigit():
        raise ValueError
    number = int(number)
    date_obj = datetime.strptime(date, "%Y%m%d").date()
    number_dict = storage.get(date_obj.year)
    if not number_dict:
        number_dict = {}
    number_dict[date_obj.month] = number
    storage[date_obj.year] = number_dict
    return f"Data was successfully recorded: year:{date_obj.year}, month:{date_obj.month}, amount:{number}"


@app.route("/calculate/<year>")
def calculate_year(year):
    if datetime.now().year < int(year) or not year.isdigit():
        raise ValueError
    year = int(year)
    summ = 0
    amounts = storage.get(year)
    if amounts:
        for s in amounts.values():
            summ += int(s)
        return f"Amount for {year} year is {summ}"
    return f"no Information about {year} year"

@app.route("/calculate/<int:year>/<month>")
def calculate_month(year: int, month):
    # print(datetime.now().year)
    # print(datetime.now().month)
    # print(year)
    # print(month)
    # print("8()0".isdigit())
    # print('--------------------------------------')
    if (not str(year).isdigit() or not str(month).isdigit() or (datetime.now().year == year and datetime.now().month < int(month)) or int(month) < 1 or int(month) > 12 or datetime.now().year < year):
        raise ValueError
    month = int(month)
    year = int(year)
    amounts = storage.get(year)
    if amounts:
        summ = amounts.get(month)
        if summ:
            return f"Amount for {year} year, {month} month is {summ}"
        return f"no Information about {year} year {month} month"
    return f"no Information about {year} year"


if __name__ == "__main__":
    app.run(debug=True)
