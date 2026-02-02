_ = input()
a = [int(x) for x in input().split()]
r = 0
for i in range(len(a)):
    if i != len(a)-1:
        r += a[i] - 1
    else:
        r += a[i]
print(r)
