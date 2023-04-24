import unittest

from ex_1 import hello
from ex_2 import policz_studentow
from ex_3 import policz_studentow_plec
from ex_4 import oblicz_potega
from ex_5 import nawiasy
from ex_6 import para_nawiasow
from ex_7 import wykres
from ex_8 import funkcja_liniowa


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

    def test_nawiasy(self):
        tekst_1 = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)))"
        tekst_2 = "edbw(hda"
        tekst_3 = "adgjesh(((((}}"
        tekst_4 = "2136872bfewo9433n00m[][][][]))"
        self.assertEqual(nawiasy(tekst_1), [4, 6])
        self.assertEqual(nawiasy(tekst_2), [1, 0])
        self.assertEqual(nawiasy(tekst_3), [5, 2])
        self.assertEqual(nawiasy(tekst_4), [4, 6])

    def test_para_nawiasow(self):
        tekst_1 = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
        tekst_2 = "edbw()hda[]"
        tekst_3 = "adgjesh((}}"
        tekst_4 = "2136872bfewo9433n00m{{[][][][]))"
        self.assertTrue(para_nawiasow(tekst_1))
        self.assertTrue(para_nawiasow(tekst_2))
        self.assertFalse(para_nawiasow(tekst_3))
        self.assertFalse(para_nawiasow(tekst_4))

    def test_wykres(self):
        wykres_1 = [[2, 4], [4, 4], [6, 4]]
        wykres_2 = [[2, 3], [4, 4], [6, 5]]
        wykres_3 = [[2, 3], [4, 3], [5, 4]]
        self.assertTrue(wykres(wykres_1))
        self.assertTrue(wykres(wykres_2))
        self.assertFalse(wykres(wykres_3))

    def test_funkcja_liniowa(self):
        punkty_1 = [[2, 4], [4, 4]]
        punkty_2 = [[2, 3], [4, 4]]
        punkty_3 = [[2, 3], [4, 3]]
        punkty_4 = [[1.5, 3.8], [4.2, 2.9]]
        self.assertTrue(funkcja_liniowa(punkty_1))
        self.assertTrue(funkcja_liniowa(punkty_2))
        self.assertTrue(funkcja_liniowa(punkty_3))
        self.assertFalse(funkcja_liniowa(punkty_4))







if __name__ == '__main__':
    unittest.main()
