import numpy as np

n,m = [int(x) for x in input().split()]

arr = np.zeros((n,m), np.int64)

for i in range(n):
    arr[i] = [int(x) for x in input().split()]

x = arr.min(1).max()
y = arr.max(0).min()
print(x,y)