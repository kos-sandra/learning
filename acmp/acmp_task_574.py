s1 = input()
s2 = input()
count = {}
for x in s1:
    count[x] = 0

for x in s1:
    count[x] += 1

for x in s2:
    if x not in count:
        print("NO")
        break
    else:
        count[x] -= 1
        if count[x] < 0:
            print("NO")
            break
else:
    for x in count:
        if count[x] != 0:
            print("NO")
            break
    else:
        print("YES")

# print("YES" if sorted(input()) == sorted(input()) else "NO")