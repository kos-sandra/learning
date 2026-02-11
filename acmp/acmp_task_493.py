n,m = [int(x) for x in input().split()]
r = 0

c = []
for x in range(n):
    s = input()
    c.append(s)

for x in range(n):
    for y in range(m):
        b = c[x][y] == '.'
        b1 = x == 0 or c[x-1][y] == '.'
        b2 = y == 0 or c[x][y-1] == '.'
        b3 = y == m-1 or c[x][y+1] == '.'
        b4 = x == n-1 or c[x+1][y] == '.'
        if all((b,b1,b2,b3,b4)):
            r+=1

print(r)