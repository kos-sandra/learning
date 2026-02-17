n = int(input())


def deliteli(x):
    res = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.append(i)
            res.append(x // i)
    return sorted(res)


def sum_digits(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10

    return s


res = [(sum_digits(x), -x) for x in deliteli(n)]
res = sorted(res, reverse=True)

print(-res[0][1])
