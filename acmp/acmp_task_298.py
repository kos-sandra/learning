def xy(a, b):
    return a[0], a[1], b[0], b[1]

def quarter(a, b):
    x1, y1, x2, y2 = xy(a, b)
    return (x1 * x2) >= 0 and (y1 * y2) >= 0


def collinearity(a, b):
    x1, y1, x2, y2 = xy(a, b)
    return y1 * x2 == y2 * x1


n = int(input())
res = n
m = set()

for i in range(n):
    x, y = [int(x) for x in input().split()]
    m.add((x, y))

m = list(m)
i = 0
while i < len(m):
    a = m[i]
    j = i + 1
    while j < len(m):
        b = m[j]
        if quarter(a, b) and collinearity(a,b):
            res -= 1
            m.remove(b)
        else:
            j += 1
        print(a, b, quarter(a, b) and collinearity(a,b), res)
        print(m, len(m))
    i += 1

print(len(m))

# n = int(input())
# a = [(*map(int, input().split()),) for i in range(n)]
#
# c = 0
# while a:
#     p2 = a[0]
#     a = [p1 for p1 in a if p1[0] * p2[0] < 0 or p1[1] * p2[1] < 0 or p1[0] * p2[1] != p2[0] * p1[1]]
#     c += 1
# print(c)
