field = input(), input(), input()


def xoxoxo(a, b, c, found):
    if found:
        return True
    if a == b and a == c:
        if a == "X":
            print("Win")
            return True
        if a == "O":
            print("Lose")
            return True
    return False


found = False

found = found or xoxoxo(field[0][0], field[0][1], field[0][2], found)
found = found or xoxoxo(field[1][0], field[1][1], field[1][2], found)
found = found or xoxoxo(field[2][0], field[2][1], field[2][2], found)
found = found or xoxoxo(field[0][0], field[1][0], field[2][0], found)
found = found or xoxoxo(field[0][1], field[1][1], field[2][1], found)
found = found or xoxoxo(field[0][2], field[1][2], field[2][2], found)
found = found or xoxoxo(field[0][0], field[1][1], field[2][2], found)
found = found or xoxoxo(field[0][2], field[1][1], field[2][0], found)
if not found:
    print("Draw")
