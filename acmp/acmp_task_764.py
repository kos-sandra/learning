def pifagor(a,b):
    return (a**2 + b**2)**0.5

def norm(v):
    l = pifagor(*v)
    return v[0] / l, v[1] / l

def equals(v1,v2):
    return all(abs(x-y) <= 1e-6 for x,y in zip(v1,v2))


n = int(input())

dots = []

for i in range(n):
    dots.append([int(x) for x in input().split()])

counts = []

for i in range(n):
    count = 0
    v1 = norm(dots[i])
    for j in range(n):
        v2 = norm(dots[j])
        if equals(v1,v2):
            count += 1
    counts.append(count)

print(max(counts))