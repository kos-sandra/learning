import numpy as np

n = int(input())

p = np.array([0., 0.])
a = (2 ** 0.5) / 2
d = np.array([
    [0, 0],
    [0, 1],
    [a, a],
    [1, 0],
    [a, -a],
    [0, -1],
    [-a, -a],
    [-1, 0],
    [-a, a],
])

for i in range(n):
    dir, steps = [int(x) for x in input().split()]
    p += d[dir] * steps

print(*p)

# print(d > 0)
# mask_axis0 = np.any(d > 0, 0)
# mask_axis1 = np.any(d > 0, 1)
# print(mask_axis0)
# print(mask_axis1)
# print(d[..., mask_axis0])
# print(d[mask_axis1])
