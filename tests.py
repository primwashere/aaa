from ex_1 import *
from unittest.mock import patch
import unittest

@patch('builtins.print')
def test_hello(mock_print):
    hello("Ola")
    mock_print.assert_called_with("Hello Ola")
    hello("Zuzia")
    mock_print.assert_called_with("Hello Zuzia")

    import sys
    sys.stdout.write(str( mock_print.call_args ) + '\n')
    sys.stdout.write(str( mock_print.call_args_list ) + '\n')

if __name__ == '__main__':
    test_hello()
