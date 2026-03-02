def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    B = x1 - x2
    A = y1 - y2
    return (A ** 2 + B ** 2) ** 0.5


n, c, p = [int(x) for x in input().split()]

dots = []
edges = []

for i in range(n):
    dots.append([int(x) for x in input().split()])
d0 = [int(x) for x in input().split()]

avg = sum(x[0] for x in dots) / n, sum(x[1] for x in dots) / n

distances = map(lambda d: distance(avg, d), dots)
min_dist = min(distances)
closest_dots = []
for d in dots:
    if distance(avg, d) == min_dist:
        closest_dots.append(d)
optimal_dot = closest_dots[0]
for d in closest_dots:
    if distance(d, d0) < distance(optimal_dot, d0):
        optimal_dot = d

length = distance(optimal_dot, d0) + sum(distance(d, optimal_dot) for d in dots)
print('YES' if length * c <= p else 'NO')
