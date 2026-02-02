s, R = [int(x) for x in input().split()]
p = 0
r = 100001
for i in range(s):
    p2 = input()
    r2 = sum([int(x) for x in input().split()])
    if r2 < r:
        r = r2
        p = p2
print(p)