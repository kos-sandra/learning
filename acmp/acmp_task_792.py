n = int(input())
a = []
if n > 8:
    a.append(n - 8)
if n % 8 != 1:
    a.append(n - 1)
if n % 8 != 0:
    a.append(n + 1)
if n <= 56:
    a.append(n + 8)
print(*a)