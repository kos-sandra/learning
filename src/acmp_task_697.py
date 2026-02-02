l,w, h = input().split()
b = ((int(l) * int(h)) * 2) + ((int(w) * int(h)) * 2)
r = 16
if b < r:
    print(1)
elif b % r == 0:
    print(b // r)
else:
    print(b // r + 1)