def qua(res, i, j):
    for I in range(i-1,i+2):
        if -1 < I < len(res):
            for J in range(j-1,j+2):
                if -1 < J < len(res[0]) and res[I][J] != '*':
                    res[I][J] += 1


N, M, k = [int(x) for x in input().split()]

res = []
for i in range(N):
    res.append([])
    for j in range(M):
        res[i].append(0)

for i in range(k):
    n, m = [int(x) for x in input().split()]
    res[n-1][m-1] = '*'

for i in range(N):
    for j in range(M):
        if res[i][j] == '*':
            qua(res, i,j)

for i in range(N):
    for j in range(M):
        if res[i][j] == 0:
            res[i][j] = '.'
        print(res[i][j],end='')
    print()
