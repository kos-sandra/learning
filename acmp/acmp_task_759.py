n,m = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
L = []
for x in l:
    if x >= 0:
        L.append(x)

L.sort(reverse=True)
v = sum(L[:m])
print(v)