start, finish = [x for x in input().split()]

x_coordinates = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x1, y1 = x_coordinates[start[0]], int(start[1])
x2, y2 = x_coordinates[finish[0]], int(finish[1])

diff_x, diff_y = abs(x2 - x1), y2 - y1
diff = (diff_x - diff_y) % 2

print("YES" if diff == 0 and diff_x <= diff_y and diff_y > 0 else "NO")
