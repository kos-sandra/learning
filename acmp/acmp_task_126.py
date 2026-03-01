n = int(input())
m = []
for i in range(n):
    m.append([int(x) for x in input().split()])

x = 9999
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x = min(x, m[i][j] + m[j][k] + m[k][i])
print(x)