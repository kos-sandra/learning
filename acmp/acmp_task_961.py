n,m = [int(x) for x in input().split()]
matrix1 = [input() for _ in range(n)]
input()
matrix2 = [input() for _ in range(n)]

objects = []

for i in range(n):
    for j in range(m):
        x = matrix1[i][j]
        y = matrix2[i][j]
        if x != y and x != '.':
            objects.append(x)

if len(objects) > 0:
    print(len(objects))
    objects = sorted(objects, key=lambda c: (0 if c.islower() else 1, c))
    print(*objects, sep='')
else:
    print(0)

