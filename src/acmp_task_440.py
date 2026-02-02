hits = set()

for i in range(5):
    x, y = [int(i) for i in input().split()]
    for x0 in range(0, 125, 25):
        if ((x - x0) ** 2 + y * y) <= 100:
            hits.add(x0)

print(len(hits))
