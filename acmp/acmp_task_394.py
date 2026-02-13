def nod(a, b):
    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a, b = b, a % b
    return b


def nok(a, b):
    return a * b // nod(a, b)


n, m = [int(x) for x in input().split()]

print(nok(n,m)//m)
