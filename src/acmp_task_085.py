a, b = [int(x) for x in input().split()]


def onek(a):
    r = ''
    for i in range(a):
        r += '1'
    return int(r)


a, b = onek(a), onek(b)


def evkl(a,b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        d = a % b
        a, b = b, d
    return a

print(evkl(a,b))
