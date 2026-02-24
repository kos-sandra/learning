def comparison(s1,s2):
    total = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            total += 1
    return total


s = input()
m = int(input())

res = []
min_v = len(s)

for i in range(m):
    x = input()
    diffrence = comparison(s, x)
    res.append([diffrence, i + 1])
    if diffrence < min_v:
        min_v = diffrence

res.sort()

res = list(map(lambda x:x[1], filter(lambda x: x[0] == min_v, res)))

print(len(res))
print(*res)