a = int(input())
s = 0


def nod(a, b):
    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a, b = b, a % b
    return b


for x in range(1,a):
    if nod(a,x) == 1:
        s += 1

print(s)