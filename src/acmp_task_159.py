n = int(input())
k = [int(x) for x in input().split()]
new = [0 for i in range(n)]

for i in range(n):
    new[k[i] - 1] = i + 1

print(*new)