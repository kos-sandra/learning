n = int(input())
a = [int(x) for x in input().split()]
m = int(input())
for _ in range(m):
    ik, jk = [int(x) for x in input().split()]
    ik = ik - 1
    for i in range(ik, jk):
        print(a[i], end=' ')
    print()
