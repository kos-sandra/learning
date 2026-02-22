a,b,r = [float(x) for x in input().split()]

x = r / (1 + b ** 2 / a ** 2) ** 0.5
y = b * x / a
res = a * x + b * y

print(res)
print(x, y)
