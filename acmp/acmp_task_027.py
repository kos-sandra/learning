w, h = [int(x) for x in input().split()]
n = int(input())

squares = []
for i in range(n):
    s = tuple(int(x) for x in input().split())
    squares.append((abs(s[2] - s[0]) * abs(s[3] - s[1]), s[0], s[1], s[2], s[3]))
squares.sort(reverse=True)


field = [[1 for i in range(w)] for j in range(h)]

for x in range(w):
    for y in range(h):
        for s in squares:
            S, x1, y1, x2, y2 = s
            if x1 <= x < x2 and y1 <= y < y2:
                field[y][x] = 0
                break

print(sum(sum(x) for x in field))
