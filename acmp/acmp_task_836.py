def octo(x):
    s = []
    while x > 0:
        s.append(x % 8)
        x //= 8
    s.reverse()
    return s[-3]

_ = int(input())
m = [int(x) for x in input().split()]

res = []

for x in m:
    if x % 2 == 0:
        if octo(x) % 2 > 0:
            res.append(x)

res.sort()

print(len(res))
print(*res)