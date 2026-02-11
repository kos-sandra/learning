b1 = [int(x) for x in input().split()]
g1 = [int(x) for x in input().split()]
b = b1[0] * (100 - b1[1]) / 100
b2 = b1[0] * b1[1] / 100 * b1[2]
g = g1[0] * (100 - g1[1]) / 100
g2 = g1[0] * g1[1] / 100 * g1[2]
if b > g:
    d = (b - g) * b1[2]
else:
    d = (g - b) * g1[2]
print(int(d + b2 + g2))