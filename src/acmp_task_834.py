import math

def gipotenuza(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def distance(x1, y1, x2, y2):
    return gipotenuza(x2 - x1, y2 - y1)

x1, y1 = [float(x) for x in input().split()]
x, y, r = [float(x) for x in input().split()]

a = distance(x1, y1, x, y)
if a > r:
    b = gipotenuza(a, r)
    alpha = math.asin(r / a)
    s_triangles = r * a * math.cos(alpha)
    s_sectors = r ** 2 * alpha
    print(math.pi * r ** 2 / 2 + s_sectors + s_triangles)
else:
    print(math.pi * r ** 2)
