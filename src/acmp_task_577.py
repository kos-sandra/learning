a, b = [int(x) for x in input().split()]
d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for x in range(1, a + 1):
    for y in range(1, b + 1):
        z = x * y
        while z > 0:
            d[z % 10] += 1
            z = z // 10
for i in range(len(d)):
    print(d[i])
