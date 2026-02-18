p = [int(x) for x in input().split()]
max_even = []
min_odd = []

for i in range(len(p)):
    x = p[i]
    if (i+1) % 2 == 0:
        max_even.append(x)
    if (i+1) % 2 == 1:
        min_odd.append(x)

print(max(max_even)+min(min_odd))