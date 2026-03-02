n,m = [int(x) for x in input().split()]

k_prev = 1
res = 0

for i in range(1, n+1):
    k_prev = (k_prev * 2 * i) % m
    res += k_prev

print(res%m)
