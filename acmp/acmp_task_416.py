letters = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
s = input()
x = letters.index(s[0])
y = int(s[1])

points = []
for dx in [-1, 1]:
    for dy in [-1, 1]:
        points.append((x + 2 * dx, y + dy))
        points.append((x + dx, y + 2 * dy))

points = sorted(
    map(lambda p: letters[p[0]] + str(p[1]),
        filter(lambda p: 0 < p[0] < 9 and 0 < p[1] < 9,
               points)))
print(*points, sep='\n')
