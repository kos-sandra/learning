N, w, d, P = [int(x) for x in input().split()]

s = N * (N - 1) * w // 2

x = (s - P) // d
print(x or N)