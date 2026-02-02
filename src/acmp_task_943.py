# N - количество строк матрицы
# M - количество столбцов матриц
# строки Y
# столбца X

N, M, Y, X = [int(j) for j in input().split()]
rows = []
for i in range(N):
    if i % 2 == 0:
        rows.append([j + (M * i) for j in range(M)])
    else:
        rows.append([j + (M * i - 1) for j in range(M, 0, -1)])
print(rows[Y-1][X-1])

