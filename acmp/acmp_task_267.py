n,m = [int(x) for x in input().split()]
y = n // m
r = []
d = n % m

for x in range(m-d):
    r.append(y)

for i in range(d):
    r.append(y+1)

print(*r, sep=' ')