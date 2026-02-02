n, m, k = [int(x) for x in input().split()]
if k > m:
    print(m*n)
else:
    b = m // k
    a = k-1
    print((a + b) * n)
