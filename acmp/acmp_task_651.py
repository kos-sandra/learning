# def decompose(n):
#     res = {}
#     d = 2
#     while n > 1 and d <= n**0.5:
#         while n % d == 0:
#             n //= d
#             if d not in res:
#                 res[d] = 0
#             res[d] += 1
#         d += 1
#     if n > 1:
#         res[n] = 1
#     return res
#
#
# n, m = [int(x) for x in input().split()]
#
# d1 = decompose(n)
# d2 = decompose(m)
#
# primes = set(d1.keys()) | set(d2.keys())
# c = 0
#
# for d in primes:
#     c += abs(d1.get(d, 0) - d2.get(d, 0))
#
# print(c)

def nod(a, b):
    a, b = sorted([a, b])
    while b > 0:
        a, b = b, a % b
    return a

def count_d(n):
    c = 0
    d = 2
    while n > 1 and d <= n**0.5:
        while n % d == 0:
            n //= d
            c += 1
        d += 1
    if n > 1:
        c += 1
    return c


n, m = [int(x) for x in input().split()]

o = nod(n, m)
n //= o
m //= o

print(count_d(n) + count_d(m))