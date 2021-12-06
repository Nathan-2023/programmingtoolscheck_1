import unittest
from main import print_hi_stephen, print_hi_you, print_hi_jerry  # , print_hi_?


class MyTestCase(unittest.TestCase):
    def test_print_hi_stephen(self):
        self.assertEqual(print_hi_stephen(), f"Hi, Stephen")


    def test_print_hi_you(self):
        self.assertEqual(print_hi_you(), f"Hi, you")

    def test_print_hi_(self):
        self.assertEqual(print_hi_jerry(), f"Hi, jerry")


if __name__ == '__main__':
    unittest.main()
