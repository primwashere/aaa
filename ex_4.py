# Zaokraglij do dwoch miejsc po przecinku
# def oblicz_potega(liczba, potega) -> float:
#     return 0

def oblicz_potega(liczba, potega) -> float:
    wynik = liczba ** potega
    wynik_zaokraglony = round(wynik, 2)
    return wynik_zaokraglony

# print(oblicz_potega(1.234, 2.456))