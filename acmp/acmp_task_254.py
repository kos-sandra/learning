n = int(input())
priest = input().split()
m = int(input())
zayavki = {}
for i in range(m):
    before,after = input().split()
    zayavki[before] = after

for i in range(n):
    x = priest[i]
    if x in zayavki:
        priest[i] = zayavki[x]

print(*priest)