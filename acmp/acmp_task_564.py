def s(a, b, c):
    p = (a + b + c) / 2
    d = (p * (p - a) * (p - b) * (p - c))
    return d ** 0.5 if d > 0 else -1


n = int(input())
z = [int(x) for x in input().split()]
max_s = -1
a, b, c = 0, 0, 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            ploshad = s(z[i], z[j], z[k])
            if ploshad > 0 and max_s < ploshad:
                max_s = ploshad
                a, b, c = i + 1, j + 1, k + 1

print(max_s)
if max_s > 0:
    print(a, b, c)
