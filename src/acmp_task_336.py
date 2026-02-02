o = 0
l = {0}
for x in input():
    if x == "1":
        o += 1
    else:
        o += - 1
    l.add(o)
print(len(l))