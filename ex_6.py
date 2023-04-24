def para_nawiasow(tekst: str) -> bool:
    count = 0
    for i in tekst:
        if i == "(" or i == '[' or i == '{':
            count += 1
        elif i == ')' or i == '[' or i == '{':
            count -= 1
        if count < 0:
            return False
        if count == 0:
            return True
        return False

tekst_1 = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
tekst_4 = "2136872bfewo9433n00m{{[][][][]))"
print(para_nawiasow(tekst_1))
print(para_nawiasow(tekst_4))

