n = int(input())
p = [int(x) for x in input().split()]
p.sort()

r = [0 for i in range(n)]
j = 0
for j in range(n):
    i = j // 2 if j % 2 == 0 else n - 1 - j // 2
    r[i] = p[j]
print(*r)