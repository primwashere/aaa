# Policz studentki i studentow i zwroc wynik w formacie: [k, m]
# Przyjmij, ze imie dla kobiety konczy sie na "a"
# def policz_studentow_plec(studenci) -> [int, int]:
#     return [0, 0]
def policz_studentow_plec(studenci) -> [int, int]:
    liczba_kobiet = 0
    liczba_mezczyzn = 0
    for dane in studenci:
        if isinstance(dane, str):
            imie = dane.split()[0]
            if imie[-1] == 'a':
                liczba_kobiet += 1
            else:
                liczba_mezczyzn += 1
    return [liczba_mezczyzn, liczba_kobiet]

print(policz_studentow_plec([17, 12, "Ola Hamrol", "Ania Oleksy", "Piotr Kawa", "Basia Kwiatkowski", "Marek Rydz"]))