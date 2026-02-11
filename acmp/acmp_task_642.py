N,S = input().split()
N,S = int(N), int(S)
r = 0
l = []
for x in input().split():
    l.append(int(x))
l.sort()
for x in l:
    if S - x >= 0:
        S = S - x
        r += 1
print(r)