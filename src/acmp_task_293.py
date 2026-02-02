N = int(input())
V = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
r = 1
c = 0
for i in range(N):
    p = V[i] * (P[i] / 100)
    if  p > c:
        c = p
        r = i+1
print(r)