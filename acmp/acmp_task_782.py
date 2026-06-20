n = int(input())

res = 0
if n > 3:
    res += 1

if n == 0:
    print(0)
else:
    while n > 1:
        d = n // 2
        n = d + n % 2
        res += d
    print(res)