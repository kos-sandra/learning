n, k = map(int, input().split())
print([n**n - n * k + k, 7][n < 3])
