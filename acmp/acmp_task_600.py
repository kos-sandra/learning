n = int(input())

for i in range(n):
    x = list(input())
    if len(x) < 3:
        print("NO")
        continue
    if x != sorted(x):
        print("NO")
        continue
    counts = {}
    for k in x:
        if k not in counts:
            counts[k] = 1
        else:
            counts[k] += 1
    if counts['0'] == counts['1'] == counts['2']:
        print("YES")
    else:
        print("NO")
