import unittest
from module_02_linux.homework.hw7.accounting import app, storage


class TestAcountingAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.base_url: str = '/add/'

    def test_can_get_correct_reponse_add(self):
        dates = ('20150708', '20150623', '20190504', '20200312')
        for date in dates:
            with self.subTest(date=date):
                url = self.base_url + date + "/500"
                response = self.app.get(url)
                response_text = response.data.decode()
                self.assertTrue(date[:4] in response_text and str(int(date[4:6])) in response_text and "500" in response_text)

    def test_can_get_incorrect_date_add(self):
        dates = ('20504513', '2())', 'wdeafef')
        for date in dates:
            with self.subTest(date=date):
                url = self.base_url + date + "/500"
                with self.assertRaises(ValueError):
                    response = self.app.get(url)
                    response_text = response.data.decode()

    def test_can_get_incorrect_number_add(self):
        dates = ('-1100', '2())', 'wdeafef')
        for date in dates:
            with self.subTest(date=date):
                url = self.base_url + "20150125/" + date
                with self.assertRaises(ValueError):
                    response = self.app.get(url)
                    response_text = response.data.decode()


class TestAcountingCalculate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.app.get("/add/20150708/500")
        cls.app.get("/add/20150623/600")
        cls.app.get("/add/20190504/700")
        cls.app.get("/add/20200312/800")
        cls.base_url: str = '/calculate/'

    def test_can_get_correct_reponse_calculate_year(self):
        dates = (('2015', '1100'), ('2019', '700'), ('2020', '800'), ('1100', "no"))
        for date in dates:
            with self.subTest(date=date):
                url = self.base_url + str(date[0])
                response = self.app.get(url)
                response_text = response.data.decode()
                self.assertTrue(str(date[1]) in response_text)

    def test_can_get_correct_reponse_calculate_year_month(self):
        dates = (('2015/7', '500'), ('2019/5', '700'), ('2020/3', '800'), ('1100/4', "no"))
        for date in dates:
            with self.subTest(date=date):
                url = self.base_url + date[0]
                response = self.app.get(url)
                response_text = response.data.decode()
                self.assertTrue(date[1] in response_text)


    def test_can_get_incorrect_year_calculate(self):
        dates = ('2055', '2())', 'wdeafef')

        for date in dates:
            with self.subTest(date=date):
                url = self.base_url + date
                with self.assertRaises(ValueError):
                    response = self.app.get(url)
                    response_text = response.data.decode()

    def test_can_get_incorrect_month_calculate(self):
        dates = ('2015/20', '2024/12', '2020/-3', '2222/2')
        for date in dates:
            with self.subTest(date=date):
                url = self.base_url + date
                with self.assertRaises(ValueError):
                    response = self.app.get(url)
                    response_text = response.data.decode()

