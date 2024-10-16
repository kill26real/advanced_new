import unittest
from freezegun import freeze_time
from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import app, GREETINGS
import datetime


@freeze_time("2024-10-7")
def test():
    assert datetime.datetime.now() == datetime.datetime(2024, 10, 7)

@freeze_time("2024-10-8")
class MyTests(unittest.TestCase):
    def test_the_class(self):
        assert datetime.datetime.now() == datetime.datetime(2024, 10, 8)

@freeze_time("2024-10-9")
class Tester(object):
    def test_the_class(self):
        assert datetime.datetime.now() == datetime.datetime(2024, 10, 9)

@freeze_time("2024-10-10")
def test2():
    assert datetime.datetime.now() == datetime.datetime(2024, 10, 10)

@freeze_time("2024-10-11")
class MyTests2(unittest.TestCase):
    def test_the_class(self):
        assert datetime.datetime.now() == datetime.datetime(2024, 10, 11)

@freeze_time("2024-10-12")
class Tester2(object):
    def test_the_class(self):
        assert datetime.datetime.now() == datetime.datetime(2024, 10, 12)

@freeze_time("2024-10-13")
class Tester3(object):
    def test_the_class(self):
        assert datetime.datetime.now() == datetime.datetime(2024, 10, 13)



class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_reponse_with_username(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    def test_can_raise_error_username(self):
        username = 'Хорошей среды'
        with self.assertRaises(ValueError):
            response = self.app.get(self.base_url + username)
            response_text = response.data.decode()

    @freeze_time('2024-10-7')
    def test_monday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[datetime.date.today().weekday()] in response_text)

    @freeze_time('2024-10-8')
    def test_tuesday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(GREETINGS[datetime.date.today().weekday()] in response_text)

    @freeze_time('2024-10-9')
    def test_wednesday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertIn(GREETINGS[datetime.date.today().weekday()], response_text)

    @freeze_time('2024-10-10')
    def test_thursday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertIn(GREETINGS[datetime.date.today().weekday()], response_text)

    @freeze_time('2024-10-11')
    def test_friday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertIn(GREETINGS[datetime.date.today().weekday()], response_text)

    @freeze_time('2024-10-12')
    def test_saturday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertIn(GREETINGS[datetime.date.today().weekday()], response_text)

    @freeze_time('2024-10-13')
    def test_sunday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertIn(GREETINGS[datetime.date.today().weekday()], response_text)