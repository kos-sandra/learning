def is_simple(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def find_divisors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)
    return sorted(res)


n = int(input())
divs = filter(is_simple, find_divisors(n))
res = []
for d in divs:
    while n % d == 0:
        res.append(d)
        n //= d

print(*res, sep='*')