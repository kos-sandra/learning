n = input().split()
s, t = int(n[0]), int(n[1])
if t > s:
    print(t - s)
else:
    print(12 - s + t)