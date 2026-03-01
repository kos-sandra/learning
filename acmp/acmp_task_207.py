n = int(input())

x, y = 0, 0
a = (2 ** 0.5) / 2
directions = {1: (0, 1),
              2: (a, a),
              3: (1, 0),
              4: (a, -a),
              5: (0, -1),
              6: (-a, -a),
              7: (-1, 0),
              8: (-a, a)}

for i in range(n):
    dir, steps = [int(x) for x in input().split()]
    dx, dy = directions[dir]
    dx, dy = dx * steps, dy * steps
    x,y = x+dx, y + dy

print(x,y)
