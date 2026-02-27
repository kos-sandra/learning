n = int(input())
c = 0
while n > 1:
    n = (n-1)//3+1
    c += 1
print(c)