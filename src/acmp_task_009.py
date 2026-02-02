i = int(input())
N = []
for x in input().split():
    N.append(int(x))


s = 0
p = 1

for x in N:
    if x > 0:
        s += x

pos = []
pos.sort()


for z in range(i):
    if N[z] == max(N) or N[z] == min(N):
        pos.append(z)

for y in range(i):
    if y > pos[0] and y < pos[1]:
        p *= N[y]

print(s, p)