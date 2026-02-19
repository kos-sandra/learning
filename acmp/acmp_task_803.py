a,b,k = [int(x) for x in input().split()]

a = a % b
res = 0

for i in range(k):
    a *= 10
    res = a // b
    a = a % b


print(res)
