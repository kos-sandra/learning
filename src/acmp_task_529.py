n = input().split()
x, y, X, Y = int(n[0]), int(n[1]), int(n[2]), int(n[3])
a = Y - y
b = X - x
C = a**2 + b**2
c = C ** 0.5
print(round(c, 5))