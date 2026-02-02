n = int(input())
w = [int(x) for x in input().split()]
w.append(w[0])
w.append(w[1])
res = 0
for i in range(n):
    res = max(res, sum(w[i:i + 3]))
print(res)