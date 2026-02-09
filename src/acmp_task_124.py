n,m = [int(x) for x in input().split()]
res = {i: 0 for i in range(1,n+1)}

for i in range(m):
    x, y = [int(x) for x in input().split()]
    res[x] += 1
    res[y] += 1

for i in range(1, n+1):
    print(res[i],end=' ')