n = int(input())
lifetime = [int(x) for x in input().split()]
lifetime2 = {i+1: x for i,x in enumerate(lifetime)}

z = int(input())
for x in input().split():
    x = int(x)
    key = lifetime2[x]
    if key < 0:
        pass
    else:
        lifetime2[x] -= 1

for x in lifetime2:
    if lifetime2[x] < 0:
        print("yes")
    else:
        print("no")