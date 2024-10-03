from datetime import datetime, timedelta
from flask import Flask, render_template
import random
import os
import re

app = Flask(__name__)


CARS = 'Chevrolet, Renault, Ford, Lada'

CATS = ( 'корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

with open(BOOK_FILE, 'r', encoding='utf-8') as book:
    text = book.read()
    pattern = r'\b\w+\b'
    WORDS = re.findall(pattern, text)

counter = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hello_world')
def hello():
    return 'Hallo, World!'

@app.route('/hello_all')
def hello():
    return 'Hallo, all!'


@app.route('/cars')
def cars():
    return CARS


@app.route('/cats')
def cats():
    return random.choice(CATS)


@app.route('/get_time/now')
def time_now():
    current_time = datetime.now()
    return f'Точное время: {current_time.strftime("%H:%M:%S")}'


@app.route('/get_time/future')
def time_one_hour():
    current_time = datetime.now()
    current_time_after_hour = current_time + timedelta(hours=1)
    return f'Точное время: {current_time.strftime("%H:%M:%S")} \nТочное время через час будет {current_time_after_hour.strftime("%H:%M:%S")}'


@app.route('/get_random_word')
def random_word():
    return random.choice(WORDS)


@app.route('/counter')
def counter_visits():
    global counter
    counter += 1
    return str(counter)


if __name__ == '__main__':
    app.run(debug=True)
