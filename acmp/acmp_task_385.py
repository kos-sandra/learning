def gip(d1,d2):
    x1,y1 = d1
    x2,y2 = d2
    a = (x2 - x1)**2
    b = (y2-y1)**2
    return (a+b)**0.5

n = int(input())

dots = []

for i in range(n):
    x,y = [int(x) for x in input().split()]
    dots.append([x,y])

distantions = []

for i in range(n):
    dot1 = dots[i]
    for j in range(i+1, n):
        dot2 = dots[j]
        s = gip(dot1,dot2)
        if s not in distantions:
            distantions.append(s)

distantions.sort()
print(len(distantions))
for x in distantions:
    print(x)