a, b, c, d = [int(x) for x in input().split()]
# print(*[x for x in range(-100,101) if a * x**3 + b * x ** 2 + c * x + d == 0])
for x in range(-100,101):
    if a * x**3 + b * x ** 2 + c * x + d == 0:
        print(x, end=' ')