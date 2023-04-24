# Oblicz liczbę nawiasów w zmiennej, zwroc: [otwierajace, zamykajace]

def nawiasy(tekst: str) -> [int, int]:
   otwierajace = tekst.count("(")
   zamykajace= tekst.count(")")
   return[otwierajace, zamykajace]
print(nawiasy("(sjbdsjaj)(shvhas))"))
