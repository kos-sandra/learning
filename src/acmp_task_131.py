n = int(input())
age = 0
imax = -1
for i in range(n):
    a, s = [int(x) for x in input().split()]
    if a > age and s == 1:
        age = a
        imax = i+1
print(imax)