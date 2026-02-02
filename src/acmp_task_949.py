n, a, b = (int(x) for x in input().split())
for i in range(n-1,0,-1):
    a, b = b - a, a
print(a,b)