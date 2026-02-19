field = [[0 for i in range(10)] for j in range(10)]

n = int(input())

for i in range(n):
    x, y = [int(x) for x in input().split()]
    field[x][y] = 1

res = 0

for i in range(9):
    for j in range(9):
        res += int(field[i][j] != field[i + 1][j]) \
             + int(field[i][j] != field[i][j + 1])

print(res)
