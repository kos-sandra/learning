w, h, n = [int(x) for x in input().split()]


def f(w, h, x):
    return (x // w) * (x // h)


def check(w, h, n, x):
    if f(w, h, x) < n:
        return 1
    if f(w, h, x - 1) >= n:
        return -1
    return 0


def binary_search(l, r, w, h, n):
    if check(w, h, n, r) == 0:
        return r
    while True:
        m = (l + r) // 2
        c = check(w, h, n, m)
        if c == 0:
            return m
        if c == 1:
            l = m
        else:
            r = m


print(binary_search(1, 10 ** 18, w, h, n))
