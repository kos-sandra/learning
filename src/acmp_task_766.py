p = input().split()
n, m, k = int(p[0]), int(p[1]), int(p[2])
if n * m >= k:
    print("YES")
else:
    print("NO")