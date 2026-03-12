import numpy as np

N, M, k = [int(x) for x in input().split()]

field = np.zeros((N + 2, M + 2), np.int64)

for i in range(k):
    x, y = [int(x) for x in input().split()]
    field[x, y] = 10
    field[x - 1:x + 2, y - 1:y + 2] += 1
field += ord('0')
field[field == ord('0')] = ord('.')
field[field > ord('9')] = ord('*')
v = np.vectorize(chr)
print('\n'.join(''.join(x) for x in v(field[1:-1, 1:-1])))
