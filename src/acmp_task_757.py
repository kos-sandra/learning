n = input().split()
c, h, o = [int(x) for x in n]
C = 0
H = 0
if c % 2 == 0:
    C = c // 2
else:
    C = (c-1) // 2
if h % 6 == 0:
    H = h // 6
else:
    H = (h-1) // 6
if  o < C and o < H:
    print(o)
elif C < H:
    print(C)
else:
    print(H)


# l = [int(x) for x in input().split()]
# c, h, o = l[0] // 2, l[1] // 6, l[2]
# print(min(o, c, h))