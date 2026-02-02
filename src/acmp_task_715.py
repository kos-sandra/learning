n, m = [int(x) for x in input().split()]
d1 = []
d2 = []
for x in range(n):
    d1.append(input())
# s1 = ''.join(d1)
_ = input()
for x in range(n):
    d2.append(input())
# s2 = ''.join(d2)
# print(s1,s2)

d = 0
for i in range(n):
    for j in range(m):
        if d1[i][j] == d2[i][j]:
            d += 1
print(d)