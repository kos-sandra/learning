# n,m,w,l = [int(x) for x in input().split()]
# d = m + n
# c = m * n
# sd = d * w * l
# sc = c * w * w
# print(sd - sc)

n, m, d, k = [int(x) for x in input().split()]
c = n * m
C = d ** 2 * c
N = d * k * n
M = d * k * m
print(N+M-C)
