n, m = [int(x) for x in input().split()]

min_x = n
max_x = 0
min_y = m
max_y = 0

for x in range(n):
    line = input()
    if '*' in line:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
    for y in range(m):
        if line[y] == '*':
            min_y = min(min_y, y)
            max_y = max(max_y, y)

for x in range(n):
    if min_x <= x <= max_x:
        for y in range(m):
            if min_y <= y <= max_y:
                print('*', end='')
            else:
                print('.',end='')
    else:
        print('.' * m)
    print()
