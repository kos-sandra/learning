v = input()
l = [int(x) for x in v]
b = True
for x in l:
    if x == 0:
        b = False
        print('NO')
        break
if b:
    print('YES')