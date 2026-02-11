start = [int(x) for x in input().split()]
finish = [int(x) for x in input().split()]

hh = start[0]
mm = start[1]

total = 0

while hh != finish[0] or mm != finish[1]:
    if mm == 30:
        total += 1
    if mm == 0:
        v = 12 if hh %12 == 0 else hh % 12
        total += v

    mm += 1

    if mm == 60:
        mm = 0
        hh += 1
    if hh == 24:
        hh = 0



print(total)