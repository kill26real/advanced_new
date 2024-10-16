import unittest
from module_03_ci_culture_beginning.homework.hw2.decrypt import decrypt




class TestDecrypt(unittest.TestCase):

    def test_can_get_correct_reponse_one_dot(self):
        tests = ("абра-кадабра.", ".")

        for test in tests:
            with self.subTest(test=test):
                answer_from_func = decrypt(test)
                self.assertNotIn(".", answer_from_func)


    def test_can_get_correct_reponse_two_dots(self):
        tests = ("абраа..-кадабра", "абра--..кадабра")

        for test in tests:
            with self.subTest(test=test):
                answer_from_func = decrypt(test)
                self.assertTrue(len(answer_from_func) == len(test) - 3)


    def test_can_get_correct_reponse_three_dots(self):
        tests = ("абрау...-кадабра", "абрау...-кадабра", "1..2.3")

        for test in tests:
            with self.subTest(test=test):
                answer_from_func = decrypt(test)
                self.assertTrue(len(answer_from_func) == len(test) - 4)


    def test_can_get_correct_reponse_empty(self):
        tests = ("абра........", "1.......................")

        for test in tests:
            with self.subTest(test=test):
                answer_from_func = decrypt(test)
                self.assertTrue(len(answer_from_func) == 0)


    def test_can_get_correct_reponse_alot_dots(self):
        test = "абр......a."
        answer_from_func = decrypt(test)
        self.assertEqual(answer_from_func, "a")


    def test_can_get_correct_reponse_common_form(self):
        tests = ("абра-кадабра.", "абраа..-кадабра", "абраа..-.кадабра", "абра--..кадабра", "абрау...-кадабра")

        for test in tests:
            with self.subTest(test=test):
                answer_from_func = decrypt(test)
                self.assertEqual(answer_from_func, "абра-кадабра")

