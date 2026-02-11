K, N = [int(x) for x in input().split()]
c = {0: 1}

def zay(k, n):
    if n < 0:
        return 0
    if n in c:
        return c[n]
    s = 0
    for x in range(k, 0, -1):
        s += zay(k, n - x)
    c[n] = s
    return s

print(zay(K,N))