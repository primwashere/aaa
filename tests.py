import numpy as np
import unittest

from ex_1 import hello
from ex_2 import policz_studentow

# from unittest.mock import patch


class TestClass(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("Ola"), "Hello Ola")
        self.assertEqual(hello("Kasia"), "Hello Kasia")

    def test_policz_studentow(self):
        studenci_1 = ["Ania", "Kuba", "Piotr", "Jan"]
        studenci_2 = ["Ania", "Kuba", "Piotr", "Jan", "Basia"]
        studenci_3 = ["Ania", "Kuba", "Piotr", "Jan", 0, 34, np.NaN]
        self.assertEqual(policz_studentow(studenci_1), 4)
        self.assertEqual(policz_studentow(studenci_2), 5)
        self.assertEqual(policz_studentow(studenci_3), 4)


# @patch('builtins.print')
# def test_hello(mock_print):
#     hello("Ola")
#     mock_print.assert_called_with("Hello Ola")
#     hello("Zuzia")
#     mock_print.assert_called_with("Hello Zuzia")
#
#     import sys
#     sys.stdout.write(str(mock_print.call_args) + '\n')
#     sys.stdout.write(str(mock_print.call_args_list) + '\n')
#
#
# if __name__ == '__main__':
#     test_hello()


if __name__ == '__main__':
    unittest.main()
