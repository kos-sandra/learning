x1, y1, x2, y2 = input().split()
x3, y3 = input().split()
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
x3, y3 = int(x3), int(y3)
if y2 == y1:
    x4 = x3
    y4 = y1
elif x2 == x1:
    x4 = x1
    y4 = y3
else:
    k = (y2 - y1) / (x1 - x2)
    b = y1 - k * x1
    c = y3 + x3 / k
    x4 = ((c-b) * k) / (k **2 + 1)
    y4 = k*x4 + b
x5 = x3 + 2 * (x4 - x3)
y5 = y3 + 2 * (y4-y3)
print(x5,y5)