x, y = input().split()
x, y = int(x), int(y)
if x == 1 and y == 1:
    print(0)
elif x == y:
    print(2)
else:
    print(1)
