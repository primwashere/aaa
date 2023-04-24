import unittest

from ex_1 import hello
from ex_2 import policz_studentow
from ex_3 import policz_studentow_plec
from ex_4 import oblicz_potega


# from unittest.mock import patch


class TestClass(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("Ola"), "Hello Ola")
        self.assertEqual(hello("Kasia"), "Hello Kasia")

    def test_policz_studentow(self):
        studenci_1 = ["Ania", "Kuba", "Piotr", "Jan"]
        studenci_2 = ["Ania", "Kuba", "Piotr", "Jan", "Basia"]
        studenci_3 = [15, "Ania", "Kuba", "Piotr", "Jan", 0, 34]
        self.assertEqual(policz_studentow(studenci_1), 4)
        self.assertEqual(policz_studentow(studenci_2), 5)
        self.assertEqual(policz_studentow(studenci_3), 4)

    def test_policz_studentow_plec(self):
        studenci_1 = ["Anna", "Jakub", "Piotr", "Jan"]
        studenci_2 = ["Anna Patera", "Anna Piątek", "Piotr Kawa", "Jan Mały", "Barbara Wrzesień"]
        studenci_3 = [17, "Anna Patera", "Anna Piątek", 0, "Piotr Kawa", "Jan Mały", "Barbara Wrzesień"]
        studenci_4 = [17, "Anna Patera", "Anna Piątek", 0, "Piotr Kawa", "Katarzyna", "Bartosz"]
        self.assertEqual(policz_studentow_plec(studenci_1), [1, 3])
        self.assertEqual(policz_studentow_plec(studenci_2), [3, 2])
        self.assertEqual(policz_studentow_plec(studenci_3), [3, 2])
        self.assertEqual(policz_studentow_plec(studenci_4), [3, 2])

    def test_oblicz_potega(self):
        liczba_1 = 0.59
        potega_1 = 2
        liczba_2 = 10
        potega_2 = 3
        self.assertEqual(oblicz_potega(liczba_1, potega_1), 0.35)
        self.assertEqual(oblicz_potega(liczba_2, potega_2), 1000)


if __name__ == '__main__':
    unittest.main()
