n = int(input())

k = 12
x3 = n // k**2
x2 = (n % k**2) // 12
x1 = n - k**2 * x3 - k * x2

if x1 * 10.5 > 102.5:
    x1 = 0
    x2 += 1
if x1 * 10.5 + x2 * 102.5 > 1140:
    x1 = 0
    x2 = 0
    x3 += 1

print(x3,x2,x1)