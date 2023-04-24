# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True

def wykres(wykres) -> bool:
    x1, y1 = wykres[0]
    x2, y2 = wykres[1]
    for i in range(2, len(wykres)):
        x, y = wykres[i]
        if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
            return False
    return True