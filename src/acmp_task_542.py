def to_dexi(n):
    n = str(n)
    z = len(n)
    p = list([int(x) for x in n])

    res = 0
    j = 0
    for i in range(z - 1, -1, -1):
        res += p[j] * 2 ** i
        j += 1
    return res

def


n = input()



