line = input().split()
n = int(line.pop(0))
n2 = n
k = len(line[0])

res = 1

while n > 0:
    res = res * n
    n = n - k

print(res)