n = int(input())
p = [int(x) for x in input().split()]
p.sort()
t = {}
max_pd = 1
for x in p:
    t[x] = 0
    if x > max_pd:
        max_pd = x
eratos = [1] * (max_pd + 1)
eratos[0] = eratos[1] = 0
simple_digits = []

for i in range(len(eratos)):
    if eratos[i]:
        simple_digits.append(i)
        for j in range(i*i, len(eratos),i):
            eratos[j] = 0
        for d in t:
            if d % i == 0:
                t[d] += 1

max_with_simple_delit = max(t.values())

for x in t:
    if t[x] == max_with_simple_delit:
        print(x)
        break
