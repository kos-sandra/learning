k = input().split()
x1, y1 = int(k[0]), int(k[1])
x2, y2 = int(k[2]), int(k[3])
x3, y3 = int(k[4]), int(k[5])


def dist(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return (dx ** 2 + dy ** 2) ** 0.5


a = dist(x1, y1, x2, y2)
b = dist(x2, y2, x3, y3)
c = dist(x1, y1, x3, y3)
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(round(s, 1))

