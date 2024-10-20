"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app


class RegistrationTestCase(unittest.TestCase):

    def setUp(self):
        # Настройка для каждого теста
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()


    def test_register_success(self):
        response = self.app.post('/registration', data={
            'phone': '1234567890',
            'email': 'testuser@example.com',
            'name' : 'testuser',
            'address' : 'testadress',
            'index' : 3,
            'comment': 'comment'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("testuser", response.data.decode())

    def test_register_invalid_username(self):
        username = ("", "123456")
        for n in username:
            response = self.app.post('/registration', data={
                'phone': '1234567890',
                'email': 'testuser@example.com',
                'name' : n,
                'address' : 'testadress',
                'index' : 3,
                'comment': 'my comment'
            })
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid", response.data.decode())


    def test_register_invalid_email(self):
        email = ("", "no 'at' sign", "asss@jsjdj.oeoekek")
        for e in email:
            response = self.app.post('/registration', data={
                'phone': '1234567890',
                'email': e,
                'name': "username",
                'address': 'testadress',
                'index': 3,
                'comment': 'my comment'
            })
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid", response.data.decode())

    def test_register_invalid_phone(self):
        phones = ("", "123456", "13213515648")
        for p in phones:
            response = self.app.post('/registration', data={
                'phone': p,
                'email': 'testuser@example.com',
                'name': 'username',
                'address': 'testadress',
                'index': 3,
                'comment': 'my comment'
            })
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid", response.data.decode())

    def test_register_invalid_address(self):
        addresses = ("", "123456")
        for a in addresses:
            response = self.app.post('/registration', data={
                'phone': '1234567890',
                'email': 'testuser@example.com',
                'name' : 'username',
                'address' : a,
                'index' : 3,
                'comment': 'my comment'
            })
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid", response.data.decode())


    def test_register_invalid_index(self):
        indexes = ("", "sagbfd")
        for i in indexes:
            response = self.app.post('/registration', data={
                'phone': '1234567890',
                'email': 'testuser@example.com',
                'name' : 'username',
                'address' : 'testadress',
                'index' : i,
                'comment': 'my comment'
            })
            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid", response.data.decode())

    def test_register_invalid_comment(self):
        response = self.app.post('/registration', data={
            'phone': '1234567890',
            'email': 'testuser@example.com',
            'name' : 'username',
            'address' : 'testadress',
            'index' : 3,
            'comment': '345374685'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid", response.data.decode())

    def tearDown(self):
        self.app_context.pop()


if __name__ == '__main__':
    unittest.main()
