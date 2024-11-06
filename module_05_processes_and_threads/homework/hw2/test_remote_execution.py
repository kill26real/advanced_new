import unittest
from remote_execution import app



class TestAcountingAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.base_url: str = '/run_code'

    def test_can_get_correct_reponse_print(self):
        url = self.base_url
        response = self.app.post(url, data={'code': "print('Hello')", 'timeout': 5})
        response_text = response.data.decode()

        self.assertTrue(response.status_code == 200 and "Hello" in response_text)


    def test_timeout_error(self):
        url = self.base_url
        response = self.app.post(url, data={'code': "import time\n time.sleep(10)", 'timeout': 1})
        response_text = response.data.decode()

        self.assertTrue(response.status_code == 200 and "Время исполнения кода превысило отведенное время" in response_text)

    def test_code_error(self):
        url = self.base_url
        response = self.app.post(url, data={'code': "print(8 / 0)", 'timeout': 5})
        response_text = response.data.decode()

        self.assertTrue(response.status_code == 200 and "error" in response_text)



if __name__ == '__main__':
    unittest.main()
