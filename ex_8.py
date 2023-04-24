# dla podanych dwoch punktow, oblicz, czy funkcja liniowa jest rozsnaca, czy malejaca
# dla niemalejacej zrwoc True
# dla malejacej zwroc False

# def funkcja_liniowa(punkty) -> bool:
#     return False

def funkcja_liniowa(punkty) -> bool:
    x1, y1 = punkty[0]
    x2, y2 = punkty[1]
    if x2 - x1 == 0:
        return True

    return y2 - y1 >= 0

# print(funkcja_liniowa([[1, 1], [2, 2]]))
