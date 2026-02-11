n = int(input())
b = 0
for x in range(n):
    a = int(input())
    b += a
if b > (n // 2):
    print(n-b)
else:
    print(b)