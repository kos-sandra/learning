x, y, z = input().split()
b = int(x) + int(y) - int(z)
if b < 0:
    print('Impossible')
else:
    print(b)