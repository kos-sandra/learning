a, b = [int(x) for x in input().split()]
c = (a * b) ** 0.5
if int(c) == c:
    print(int(c))
else:
    print(0)