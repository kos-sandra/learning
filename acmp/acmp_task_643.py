b = int(input())
S = 0
a = b
while a > 0:
    x = a % 2
    if x == 1:
        S += 1
    a = a // 2
print(b + S)
