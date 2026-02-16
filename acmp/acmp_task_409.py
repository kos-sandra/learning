n = int(input())
level = [int(x) for x in input().split()]

s_sum = 0

for i in range(1,n):
    a = level[i-1]
    b = level[i]
    s_sum += (a+b)/2

print(s_sum/(n-1))
