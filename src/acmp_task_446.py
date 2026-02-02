n, m = [int(x) for x in input().split()]
rgb = []
val = []
for r in range(n):
    ro = input().split()
    for row in ro:
        rgb.append(row)
for u in range(n):
    val.append(input().split())

d = {
    '0': '.',
    '1': '.B',
    '2': '.G',
    '3': '.GB',
    '4': '.R',
    '5': '.RB',
    '6': '.RG',
    '7': '.RGB'
}
check = False


def find(a, b):
    c = a.find(b)
    if c == -1:
        return False
    else:
        return True



for x in range(n):
    for y in range(m):
        if rgb[x][y] not in d[val[x][y]]:
            check = True

if check == False:
    print('YES')
else:
    print('NO')
