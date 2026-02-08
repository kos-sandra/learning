def s(x,k):
    digits = []
    while x > 0:
        digits.append(x%k)
        x //= k
    return sum(digits)


n,k1,k2 = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = []

for i in range(n):
    b.append(s(a[i],k1)*s(a[i],k2))

b.sort()
print(*b)