a, b, c = [int(x) for x in input().split()]

xx = []
flag = False

if a == 0:
    if b == c == 0:
        flag = True
    elif b != 0:
        xx.append(-c / b)
else:
    d = b * b - (4 * a * c)
    if d > 0:
        xx.append((-b - d ** 0.5) / (2 * a))
        xx.append((-b + d ** 0.5) / (2 * a))
    elif d == 0:
        xx.append(-b / (2 * a))

if flag:
    print(-1)
else:
    print(len(xx))
    xx.sort()
    for x in xx:
        print(x)
