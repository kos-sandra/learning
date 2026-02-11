def mirror(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n = n // 10
    return res

n = int(input())
counter = 0
for i in range(n):
    if i + mirror(i) == n:
        counter += 1

print(counter)