_ = int(input())
d = [int(x) for x in input().split()]
oven = []
odd = []
for x in d:
    if x % 2 == 0:
        oven.append(x)
    else:
        odd.append(x)
print(*odd)
print(*oven)
if len(oven) >= len(odd):
    print('YES')
else:
    print('NO')
