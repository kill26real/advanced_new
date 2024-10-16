import unittest
from module_03_ci_culture_beginning.homework.hw4.person import Person
from datetime import datetime
import os
import traceback

# class MyTestResult(unittest.TextTestResult):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.failures_list = []
#         self.errors_list = []
#
#     def addFailure(self, test, err):
#         super().addFailure(test, err)
#         # Преобразуем ошибку в строку вручную с помощью traceback
#         self.failures_list.append((test, ''.join(traceback.format_exception(*err))))
#
#     def addError(self, test, err):
#         super().addError(test, err)
#         # Преобразуем ошибку в строку вручную с помощью traceback
#         self.errors_list.append((test, ''.join(traceback.format_exception(*err))))
#
#     def write_errors_to_file(self):
#         root_dir = os.path.dirname(os.path.abspath(__file__))
#         error_file_path = os.path.join(root_dir, 'ERRORS.md')
#
#         if self.failures_list or self.errors_list:
#             with open(error_file_path, 'w') as f:
#                 f.write("# Ошибки, найденные во время тестов\n\n")
#
#                 if self.failures_list:
#                     f.write("## Failures\n\n")
#                     for i, (test, error) in enumerate(self.failures_list, 1):
#                         f.write(f"### {i}. Ошибка в тесте: `{test}`\n")
#                         f.write(f"#### Описание ошибки:\n\n{error}\n\n\n")
#
#                 if self.errors_list:
#                     f.write("## Errors\n\n")
#                     for i, (test, error) in enumerate(self.errors_list, 1):
#                         f.write(f"### {i}. Ошибка в тесте: `{test}`\n")
#                         f.write(f"#### Описание ошибки:\n\n{error}\n\n\n")
#         else:
#             with open(error_file_path, 'w') as f:
#                 f.write("# Ошибок не найдено, все тесты прошли успешно.\n")
#
#
# class MyTestRunner(unittest.TextTestRunner):
#     """Кастомный тестовый раннер, который использует MyTestResult и записывает ошибки в файл"""
#
#     def _makeResult(self):
#         return MyTestResult(self.stream, self.descriptions, self.verbosity)
#
#     def run(self, test):
#         result = super().run(test)  # Запускаем тесты с использованием кастомного MyTestResult
#         result.write_errors_to_file()  # После завершения тестов записываем ошибки в файл
#         return result


class TestAcountingAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.person = Person("Bob", 2020, "Lenina")


    def test_set_name(self):
        self.person.set_name("Boba")
        self.assertEqual(self.person.name, "Boba")

    def test_set_adress(self):
        self.person.set_address("Krilenko")
        self.assertEqual(self.person.address, "Krilenko")

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), "Bob")

    def test_get_adress(self):
        self.assertEqual(self.person.get_address(), "Lenina")

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), datetime.now().year - 2020)

    def test_is_homeless(self):
        self.assertEqual(self.person.is_homeless(), False)


# if __name__ == "__main__":
#     # Загружаем тесты
#     loader = unittest.TestLoader()
#     suite = loader.discover(start_dir='tests')  # Укажите вашу папку с тестами, например 'tests'
#
#     # Запускаем тесты через наш кастомный раннер
#     runner = MyTestRunner(verbosity=2)
#     runner.run(suite)