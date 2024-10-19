import unittest
from freezegun import freeze_time
from module_03_ci_culture_beginning.homework.hw1.hello_word_with_day import app, GREETINGS
from datetime import datetime, timedelta, date


@freeze_time("2024-10-8")
class MyTimeTest(unittest.TestCase):
    def test_the_class(self):
        assert datetime.now() == datetime(2024, 10, 8)


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

    def test_seven_days(self):
        start_date = datetime.now()
        for i in range(7):
            test_date = start_date + timedelta(days=i)
            with freeze_time(test_date):
                username = 'username'
                response = self.app.get(self.base_url + username)
                response_text = response.data.decode()
                self.assertTrue(GREETINGS[date.today().weekday()] in response_text)

