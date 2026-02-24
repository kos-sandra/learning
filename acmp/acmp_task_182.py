def pithagor(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2
    return (a ** 2 + b ** 2) ** 0.5


def find_free_vector(hipo_dots: tuple, coordinates):
    res = [x1, y1, x2, y2, x3, y3]
    for i in range(4):
        if hipo_dots[i] in res:
            res.remove(hipo_dots[i])
    return res


def sum_vectors(dots):
    x1,y1 = dots[0],dots[1]
    x2,y2 = dots[2],dots[3]
    return x1+x2, y1+y2


def diff_vectors(dot, dot2):
    x1, y1 = dot[0], dot[1]
    x2, y2 = dot2[0], dot2[1]
    return x1-x2, y1-y2


x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
coordinates = [x1, y1, x2, y2, x3, y3]

a = pithagor(x1, y1, x2, y2)
b = pithagor(x2, y2, x3, y3)
c = pithagor(x3, y3, x1, y1)

sides = {a: (x1, y1, x2, y2), b: (x2, y2, x3, y3), c: (x1, y1, x3, y3)}

hipo = max(a,b,c)
free_dot = find_free_vector(sides[hipo],coordinates)

result = diff_vectors(sum_vectors(sides[hipo]), free_dot)

print(*result)