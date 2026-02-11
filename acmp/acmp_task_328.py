N = int(input())
total = 0

for i in range(N + 1):
    n = N + 1 - i
    res = n * (N + 3 * i) // 2
    total += res

print(total)
