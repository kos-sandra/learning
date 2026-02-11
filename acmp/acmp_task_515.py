n = int(input())
p = [(0,0),]
g = []

for j in range(n):
    x, y = [int(i) for i in input().split()]
    p.append((x,y))

p.append((0,0))

for d in range(len(p)):
    now_x = p[d][0] - p[d-1][0]
    now_y = p[d][1] - p[d-1][1]
    gip = (now_x ** 2 + now_y ** 2) ** 0.5
    g.append(gip)

print("{:.3f}".format(sum(g)))
