# def policz_studentow(studenci) -> int:
#     return 0

def policz_studentow(studenci) -> int:
    count = 0
    for student in studenci:
        if isinstance(student, str):
            count += 1
    return count

# print(policz_studentow([15, "Ania", "Kuba", "Piotr", "Jan", 0, 34]))
