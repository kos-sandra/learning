i = input().split()
a, b, c, t = [int(x) for x in i]
y = t - a
if t < a:
    print(t * b)
elif t == a:
    print(a * b)
else:
    print(a * b + y * c)