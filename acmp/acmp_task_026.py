x1, y1, r1 = [int(x) for x in input().split()]
x2, y2, r2 = [int(x) for x in input().split()]
x = (x1 - x2) ** 2
y = (y1 - y2) ** 2
h = (x + y) ** 0.5
if max(r1,r2) > h + min(r1,r2):
    print('NO')
elif h <= r1 + r2:
    print('YES')
else:
    print('NO')