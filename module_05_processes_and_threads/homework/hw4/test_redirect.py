import unittest
from redirect import Redirect
import io
import sys


class TestRedirect(unittest.TestCase):
    def test_redirect_stdout(self):
        new_stdout = io.StringIO()
        with Redirect(stdout=new_stdout):
            print("Hello, stdout!")

        self.assertEqual(new_stdout.getvalue(), "Hello, stdout!\n")

    def test_redirect_stderr(self):
        new_stderr = io.StringIO()
        with Redirect(stderr=new_stderr):
            print("Hello, stderr!", file=sys.stderr)

        self.assertEqual(new_stderr.getvalue(), "Hello, stderr!\n")

    def test_redirect_stdout_and_stderr(self):
        new_stdout = io.StringIO()
        new_stderr = io.StringIO()
        with Redirect(stdout=new_stdout, stderr=new_stderr):
            print("Hello, stdout and stderr!")
            print("Hello, stderr!", file=sys.stderr)

        self.assertEqual(new_stdout.getvalue(), "Hello, stdout and stderr!\n")
        self.assertEqual(new_stderr.getvalue(), "Hello, stderr!\n")

    def test_restore_stdout_and_stderr(self):
        original_stdout = sys.stdout
        original_stderr = sys.stderr

        new_stdout = io.StringIO()
        new_stderr = io.StringIO()
        with Redirect(stdout=new_stdout, stderr=new_stderr):
            print("Inside redirect")
        self.assertIs(sys.stdout, original_stdout)
        self.assertIs(sys.stderr, original_stderr)




if __name__ == '__main__':
    unittest.main()
    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
