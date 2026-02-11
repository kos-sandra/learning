n = input()
c = 0

while len(n) > 1:
    s = 0
    c += 1
    for x in n:
        s += int(x)
    n = str(s)

print(n, c)