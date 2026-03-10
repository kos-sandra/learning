import numpy as np

n,m = [int(x) for x in input().split()]

matrix = []

for i in range(n):
     row = [int(x) for x in input().split()]
     matrix.append(row)

matrix = np.array(matrix)
trans = matrix.T
print(trans)
counter = 0

for i in range(n):
    min_x = min(matrix[i])
    for j in range(m):
        max_x = max(trans[j])
        x = matrix[i][j]
        if x == min_x and x == max_x:
            counter += 1
print(counter)