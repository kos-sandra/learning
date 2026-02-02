n = int(input())
r = 0
while n > 0:
    r = r + (n % 2)
    n = n // 2
print(r)
