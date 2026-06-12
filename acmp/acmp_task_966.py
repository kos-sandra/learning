n, *T, t = [[*map(int, s.split())] for s in open(0)]

V = 0

for i in range(min(t[0], 1000)):
    for s, f, v in T:
        V += v * (s <= i < f)
    if V < 0:
        V = 0

print(V)
