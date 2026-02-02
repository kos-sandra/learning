l = [int(x) for x in input().split()]
a, b = max(l), min(l)
while b > 0:
    a, b = b, a % b
print(a)