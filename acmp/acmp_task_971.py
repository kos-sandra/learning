x, y = [int(x) for x in input().split()]

if abs(x) == 10**9 or abs(y) == 10**9:
    print("NO")
else:
    xx = [x, x - 1, x + 1]
    yy = [y - 1, y + 1, y]

    a = xx[0], yy[0]
    b = xx[1], yy[1]
    c = xx[2], yy[2]
    print("YES")
    print(*a)
    print(*b)
    print(*c)