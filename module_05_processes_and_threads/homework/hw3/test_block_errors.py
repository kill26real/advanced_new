import unittest
from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):

    def test_ignore_send_exception(self):
        with BlockErrors(errors=[ValueError]):
            raise ValueError("Test ValueError")

    def test_raise_other_exception(self):
        with self.assertRaises(TypeError):
            with BlockErrors(errors=[ValueError]):
                raise TypeError("Test TypeError")

    def test_no_exception(self):
        with BlockErrors(errors=[ValueError]):
            result = 42
        self.assertEqual(result, 42)

    def test_subclass_exception_ignored(self):
        with BlockErrors(errors=[Exception]):
            raise RuntimeError("Test RuntimeError")



if __name__ == '__main__':
    unittest.main()
